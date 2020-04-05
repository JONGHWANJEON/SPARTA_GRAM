from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta  ## 제가 dbsparta 말고 db = client.abc 라고 만들면, 제 컴어에 서버에


## HTML을 주는 부분
@app.route('/')     ##@app 이부부은 꼭 저렇게 적어야 하나요?
                    ##예를 들어서,, 파이썬파일 test.py라고 만들어도. @app이렇게 해야 flask를 쓸 수 있는건가요?
                    ##바꿔고 해봤는데.. 에러가 자꾸 나길레.. 저 영역은 건들면 안되는건지..
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    review = {
        'title': title_receive,
        'author': author_receive,
        'review': review_receive
    }

    db.reviews.insert_one(review)
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})
        ##jsonify 을 이용해야 하는 이유가 뭔가요? jason화 시켜야 하는 이유가 뭔가요?

@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)