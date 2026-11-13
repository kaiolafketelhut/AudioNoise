FROM python:3.12-slim
COPY ratespiel_action.py /ratespiel_action.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
