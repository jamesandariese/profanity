# Profanity API

Check text for profanity.

## Usage

A sample test:

    docker build -t profanity .
    docker run --name profanity-api -p 57824:5000 -d --rm profanity
    sleep 20 # it takes a bit to load the model!
    curl -XPOST localhost:57824 -d $'this\ntext\nis\nclean'
    docker rm -f profanity-api

To use the API, simply pass a body to it via POST.  You will receive back
a JSON blob containing the following:

|    key    |    type    |                  description                      |
|    ---    |    ---     |                      ---                          |
| `overall` | `number`   | score of all text combined                        |
| `lines`   | `[number]` | score of individual lines                         |
| `average` | `number`   | average score of individual lines                 |
| `max`     | `number`   | max score of individual lines                     |
| `max5`    | `[string]` | contents of the highest scoring 5 lines           |

Scores are integers from 0 to 100 representing the confidence that there is
profanity present.  Higher numbers mean more confidence that there is
profanity.

### Docker/OCI

This uses containers _exclusively_ because the core of this API is a very fast
but not terribly up-to-date scikit-learn model.  In order to keep your own
system secure, it's highly recommended that you do _not_ install the
prerequisites to get this running anywhere except in its own isolated world.
