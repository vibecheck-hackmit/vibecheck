FROM condaforge/mambaforge
WORKDIR /app
COPY api .
EXPOSE 8000
RUN conda env create -f environment.yml
CMD ["conda", "run", "--no-capture-output", "-n", "vibecheck", "python", "main.py"]
