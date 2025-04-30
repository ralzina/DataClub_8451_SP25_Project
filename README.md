# Dataset Cleaning for 84.51 Project

This repository contains the code to clean the datasets associated with our project with 84.51. After running the code, you will have access to the cleaned data that was usd to generate the dashboards we uploaded to Tableau.

## Dashboards
To see our final dashboards, go to:
[Dashboards](https://public.tableau.com/app/profile/rene.alzina/viz/DataClub_84_51_final/GeneralAnalysis)

## Members
* Lindsay Abad
* Rene Alzina
* Alexis Amoranto
* Peter Bae
* Sofia Cipollone
* Lucas Dee
* Aryan Patel
* Oliver Wardhana

## Getting Started

### 1. Clone the repository

To get started, first clone the repository to your local machine:

```bash
git clone https://github.com/ralzina/DataClub_8451_SP25_Project.git
```
### 2. Install Dependencies

Simply run

```bash
make install
```
### 3. Running the Code

Once the repository is cloned and dependencies are installed, you can run the cleaning process by using make:

```bash
make
```
### 4. If you want to remove the generated datasets, you can remove them by running

```bash
make clean
```

### 5. More Information

The data used in this project is provided through the completejourney package, which pulls from the Complete Journey dataset. More about this dataset can be found at:

[Complete-Journey](https://cran.r-project.org/web/packages/completejourney/vignettes/completejourney.html)
