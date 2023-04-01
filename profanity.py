#!/usr/bin/env python3

#   Copyright 2023 James Andariese
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from flask import Flask, request, jsonify

import profanity_check

app = Flask(__name__)

@app.route('/health', methods = ['GET'])
def health():
    return 'ok'

@app.route('/', methods = ['POST'])
def success():
    if request.method == 'POST':
        txt = request.get_data()
        txt = txt.decode('utf-8')
        lines = txt.split('\n')
        raw_scores = profanity_check.predict_prob([txt] + lines)

        overall = int(raw_scores[0] * 100)
        
        raw_line_scores = raw_scores[1:]
        scores = [int(score * 100) for score in raw_line_scores]
        avg_score = int(sum(raw_line_scores)/len(raw_line_scores) * 100)
        
        return jsonify(
            overall=scores[0],
            lines=scores,
            max=max(scores),
            average=avg_score,
            max5=[l for s,l in sorted(zip(scores,lines))[-5:]],
        )

if __name__ == '__main__':
    import os
    app.run(host=os.environ.get('HOST', '0.0.0.0'), debug=True)

