
# File create to use .env in pipeline (.env is in git ignore so not on github)

echo SECRET_KEY=$SECRET_KEY >> ./.env

echo SENTRY_DSN=$SENTRY_DSN >> ./.env