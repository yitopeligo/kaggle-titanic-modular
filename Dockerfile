FROM gcr.io/deeplearning-platform-release/tf2-gpu.2-8

WORKDIR /

COPY trainer /trainer

RUN pip freeze > requirements.txt

ENTRYPOINT ["python", "-m", "trainer.task"]

