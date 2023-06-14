FROM python:3.8-slim AS compile-image

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc wget && pip install --upgrade pip

# Make sure we use the virtualenv:
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install numpy

# TA-Lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
  tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/opt/venv && \
  make && \
  make install && \ 
  pip install --global-option=build_ext --global-option="-L/opt/venv/lib" TA-Lib==0.4.24 

RUN rm -R ta-lib ta-lib-0.4.0-src.tar.gz

#install tensorflow and tensorflow-intel stable-baselines3
RUN python3 -m pip install --upgrade https://files.pythonhosted.org/packages/7e/5b/aab3b48f51ee433eba952c70362764fe80407ddd00a44784092a4acee195/intel_tensorflow-2.12.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl && \
python3 -m pip install --upgrade https://files.pythonhosted.org/packages/e4/8a/0c38f712159d698e6216a4006bc91b31ce9c3412aaeae262b07f02db1174/tensorflow-2.12.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl && \
python3 -m pip install --upgrade https://files.pythonhosted.org/packages/76/07/fb80e30764c9caf1c66d20c58ed5dea8c72c07ff7e9957f2ca9b11b2cdc8/stable_baselines3-1.8.0-py3-none-any.whl

WORKDIR /app
COPY /scr .
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

#TODO: image size reduction
#TODO: embed volumes or define sqllite tables to manage constant values
#FROM python:3.8-slim AS build-image
#COPY --from=compile-image /opt/venv /opt/venv
#
## Make sure we use the virtualenv:
#ENV PATH="/opt/venv/bin:$PATH"
#ENV LD_LIBRARY_PATH="/opt/venv/lib"