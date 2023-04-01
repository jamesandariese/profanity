FROM smizy/scikit-learn:0.20.2-alpine

RUN apk add py3-flask curl
RUN pip install profanity_check

COPY profanity.py /
ENTRYPOINT []
EXPOSE 5000
HEALTHCHECK --timeout=1s --interval=3s CMD ["curl", "-s", "http://localhost:5000"]
CMD ["python", "/profanity.py"]

