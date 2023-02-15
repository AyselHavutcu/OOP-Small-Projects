from flask.views import MethodView
from wtforms import Form,IntegerField,StringField, SubmitField
from flask import  Flask,render_template,request
from classes.calorie_class import Calorie
from classes.temperature_class import Temperature

app = Flask(__name__)


class HomePage(MethodView):

      def get(self):
          return render_template('index.html')


class CalorieCalculation(MethodView):
    def get(self):
        calorie_form = CalorieForm()
        return render_template('calorie_calculation_form.html', calorie_form=calorie_form)

    def post(self):
        calorieForm = CalorieForm(request.form)
        country = CalorieForm.country.data
        city = CalorieForm.city.data
        temperature = Temperature(country=country, city=city).get()
        calorie_object = Calorie(weight=float(calorieForm.weight.data), height=float(CalorieForm.height.data),
                                 age=float(CalorieForm.age.data), temperature=temperature)
        result = calorie_object.calculate()
        return render_template('calorie_calculation_form.html',calorie_form=calorieForm, result=result)


class CalorieForm(Form):
    weight = IntegerField("Weight:")
    height = IntegerField("Height:")
    age = IntegerField("Age:")
    country = StringField("Country: ")
    city = StringField("City: ")
    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie_calculation', view_func=CalorieCalculation.as_view('calorie_calculation_page'))

app.run(debug=True)