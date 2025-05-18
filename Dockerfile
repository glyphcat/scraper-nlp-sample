FROM python:3.9

WORKDIR /app

COPY requirements.txt .

# RUN apt-get update && apt-get upgrade -y && apt-get install gcc g++
# RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

##########
# GINZA
##########

# RUST対応
RUN pip install setuptools_rust
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
# パスが上記コマンドだけでは通らないので明示的に通す(GINZAのため)
ENV PATH="/root/.cargo/bin:$PATH"

# いらないかもしれない、怒られたので入れておく
RUN pip install pyproject-toml
# spacy高速版、エラー吐いたので一旦コメントアウト
# RUN pip install -U "spacy[apple]"
# GINZAインストール 　python -mは多分不要
RUN python -m pip install -U ginza ja_ginza


COPY ./app/ .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]