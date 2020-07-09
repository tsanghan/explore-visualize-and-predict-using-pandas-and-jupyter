FROM jupyter/datascience-notebook:ae885c0a6226

# Set the working directory
WORKDIR /home/jovyan

# Install correct versions
COPY requirements.txt /home/jovyan/requirements.txt
RUN pip install -r requirements.txt

# Add files
COPY *.ipynb /home/jovyan/
COPY Solutions /home/jovyan/solutions
COPY Class /home/jovyan/class
COPY data /home/jovyan/data
COPY postBuild /home/jovyan/postBuild

# Allow user to write to directory
USER root
RUN chown -R $NB_USER /home/jovyan \
    && chmod -R 774 /home/jovyan \
    && rmdir /home/jovyan/work \
    && /home/jovyan/postBuild
USER $NB_USER

# Expose the notebook port
EXPOSE 8888
