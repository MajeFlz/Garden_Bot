import aiomysql
from flask import Flask, jsonify, request
from app.settings import settings
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

async def get_pool() -> aiomysql.Pool:
    return await aiomysql.create_pool(**settings.database.__dict__, autocommit=True)

async def execute_query(query: str, *args) -> any:
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(query, args)
            return await cur.fetchall()

async def get_score(user_id: int) -> int:
    result = await execute_query("SELECT score FROM users WHERE user_id = %s", user_id)
    return result[0][0] if result else None

async def inc_score(user_id: int) -> int:
    result = await execute_query("UPDATE users SET score = score + 1 WHERE user_id = %s", user_id)
    return result

async def get_wallet(user_id: int) -> int:
    result = await execute_query("SELECT wallet_id FROM users WHERE user_id = %s", user_id)
    return result

async def update_wallet(user_id: int) -> int:
    result = await execute_query("UPDATE users SET wallet = wallet WHERE user_id = %s", user_id)
    return result

async def get_users() -> list:
    result = await execute_query("SELECT user_id, user_name FROM users")
    return [{'user_id': row[0], 'user_name': row[1]} for row in result]

@app.route('/api/users', methods=['GET'])
async def get_users_list():
    users = await get_users()
    return jsonify(users)

# @app.route('/api/users/wallet', methods=['GET'])
# async def get_user_wallet():
#     wallet = await get_wallet()
#     return jsonify(wallet)
#
# @app.route('/api/users/update_wallet', methods=['POST'])
# async def get_user_update_wallet():
#     users = await update_wallet()
#     return jsonify(users)

@app.route('/api/users/score', methods=['GET'])
async def get_user_score():
    data = request.json
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        user_id = int(user_id)
    except ValueError:
        return jsonify({'error': 'Invalid user ID'}), 400

    score = await get_score(user_id)
    if score is None:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'user_id': user_id, 'score': score})

@app.route('/api/users/increase-score', methods=['POST'])
async def increase_user_score():
    data = request.json
    user_id = data.get('user_id')

    if user_id is None:
        return jsonify({'error': 'User ID is required'}), 400

    try:
        user_id = int(user_id)
    except ValueError:
        return jsonify({'error': 'Invalid user ID'}), 400

    result = await inc_score(user_id)

    if result is None:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'message': 'User score increased successfully'})

if __name__ == '__main__':
    app.run(debug=True)
