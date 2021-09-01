FROM python:3.6.3

ENV LANG C.UTF-8
ENV APP_USER deploy
ENV APP_HOME /home/$APP_USER/app

# Install requirement
COPY requirements.txt .

RUN pip install -r requirements.txt

# Create app user and app home
RUN useradd --create-home ${APP_USER}
RUN mkdir -p ${APP_HOME}
RUN chown -R ${APP_USER}:${APP_USER} ${APP_HOME}

# Change working directory
WORKDIR ${APP_HOME}

# Change user
USER ${APP_USER}

# Copy source
COPY --chown=$APP_USER:$APP_USER . ./
