# NFT API Template

**Only returns token metadata after checking if the totalSupply() of a contract is greater-than-or-equal-to the token id requested.**



## Todo

- Add config/setup info to README.
- Write better description of project in README.

## Environment

- FLASK_ENV
- INFURA_URL
- CONTRACT_ADDRESS

## Install Deps

```bash
pipenv install
```

## Run

```bash
pipenv run flask run
```



# Deploy

## Create new ElasticBeanstalk app

```bash
eb init
eb create ENV_NAME
```

# Deploy

```bash
eb deploy
```
