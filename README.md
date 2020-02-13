# Getting started with pandas and Mastering pandas (formerly Explore, visualize, and predict using pandas and jupyter)

![Powered by Jupyter Logo](https://cdn.oreillystatic.com/images/icons/powered_by_jupyter.png)

This project contains the Jupyter Notebooks and the associated Dockerfile for Matt Harrison's courses **Getting started with Pandas** and **Mastering pandas**. Prior to June 2018, this was a two-day course entitled, **Explore, visualize, and predict using pandas and Jupyter**. It contains both the exercises and the solutions.

You can use the notebooks directly in platform [here](https://learning.oreilly.com/jupyter-notebooks/~/9781492063063).

This is a public repository so there is no need to create an account to download its contents. To download the source code from this page, click the 'Cloud' icon on the top right hand, above where the latest commit is detailed.

To download via git from your preferred terminal application, type: 

```git clone https://resources.oreilly.com/live-training/explore-visualize-and-predict-using-pandas-and-jupyter```

## Running Jupyter Locally via Docker

You will need to have Docker installed on your system to create images and run containers. You can find the installation steps for all platforms on the company's [website](https://docs.docker.com/install/)
.

1) Clone the repository for the class either using the UI or your terminal via `git clone https://resources.oreilly.com/live-training/explore-visualize-and-predict-using-pandas-and-jupyter`.

2) Once you have Docker installed, type the following on your terminal to create a Docker image: `docker build -t explore-visualize-and-predict-using-pandas-and-jupyter .`

3) That will take a little while to create a Docker image, but once completed, you can run your server with the following:
`docker run -p 8888:8888 explore-visualize-and-predict-using-pandas-and-jupyter`

4) Head to `localhost:8888` in your browser and you will be able to access the Jupyter Notebooks.
