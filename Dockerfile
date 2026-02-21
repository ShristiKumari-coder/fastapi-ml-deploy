FROM python:3.9

RUN useradd -m -u 1000 user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

# Copy requirements first
COPY --chown=user:user requirements.txt $HOME/app/requirements.txt

# Install dependencies 
# We do this as root sometimes to avoid permission issues with cache
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade -r $HOME/app/requirements.txt

# Copy the rest of the files
COPY --chown=user:user . $HOME/app

USER user

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]