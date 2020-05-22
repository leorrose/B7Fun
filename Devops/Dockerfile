FROM leorrose13/python-pillow-alpine:jenkins


RUN apk --no-cache add openssl-dev

COPY requirements.txt .

RUN pip install --upgrade pip && \
	pip install virtualenv && \
	pip install --no-cache-dir -r requirements.txt

CMD ["python"]