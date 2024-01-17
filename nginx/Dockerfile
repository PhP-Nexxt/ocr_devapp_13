FROM nginx:1.25

# Delete default .conf
RUN rm /etc/nginx/conf.d/default.conf
# Add conf path
COPY nginx.conf /etc/nginx/conf.d
