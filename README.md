# red_love
This is make for searching blood donor and make it available in online.

It's deployed on Heroku [here](http://www.redlovebd.com/donor/).

## Installation

1. `yarn install` (or `npm install`)
2. `poetry install` (or `pip install -r requirements.txt`)

## Development workflow

Run the Django server (`python manage.py runserver`) and Webpack in another tab (npx webpack --config webpack.config.js) (`yarn start`).

For more convenience you can use a tool like [Goreman](https://github.com/mattn/goreman) to run Django and Webpack in a single terminal: `goreman -f Procfile.dev start`.

## Production workflow

Compile assets first with 'npx webpack --config webpack.congif.js' or `yarn build`, then use Django collectstatic: `python manage.py collectstatic`.

If you're running on Heroku this will happen automatically if you use both the Node.js and Python buildpacks.


<!-- latest run  -->
#run
cloud_sql_proxy.exe -instances="redlove-281020:asia-south1:redlove-instance"=tcp:3308


#google cloud deploy
gcloud app deploy ./app.yaml --project=redlove-281020
