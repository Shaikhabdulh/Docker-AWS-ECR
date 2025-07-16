# Use official Nginx base image
FROM nginx:alpine

# Remove default nginx HTML files (optional)
RUN rm -rf /usr/share/nginx/html/*

# Copy custom HTML to Nginx directory
COPY index.html /usr/share/nginx/html/

# Expose port 80
EXPOSE 80
