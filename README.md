# eatsgood
![eatsgood thumbnail](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/001/582/163/datas/original.png)
- A website that allows you to make friends through food.
- eatsgood is designed to help overseas Singaporeans connect with fellow Singaporeans to combat homesickness.
- This project was done by Rachel Khan, Nem Himakshi and me for the [CodeFiesta 2021](https://codefiesta.sg/) hackathon.
- I acted as the sole developer on the team and built the minimum viable product of the website using Django and Firebase.
- For more information, you can checkout:
  - [Our hackathon submission](https://devpost.com/software/eatsgood)
  - [Our demo video](https://www.youtube.com/watch?v=c28_cuVBFHw)
  - [Our slides](https://drive.google.com/file/d/11dfTzlD_OaFeg8ywv8Fz2HFht5Aqa-ln/view?usp=sharing)
  - [Our interactive prototype](https://www.figma.com/proto/qxhsQmoZxJ9aXiiZOfzerJ/eatsgood?node-id=38%3A5&scaling=scale-down&page-id=34%3A2)
  - Our minimum viable product (taken down due to the [removal of Heroku's free plan](https://help.heroku.com/RSBRUH58/removal-of-heroku-free-product-plans-faq))

## How to Run
1. Install Python
2. `pip install -r requirements.txt`
3. `python manage.py migrate`
4. `python manage.py runserver`

## How to Compile Sass Files
- `sass --style compressed --watch index.scss index.min.css`
