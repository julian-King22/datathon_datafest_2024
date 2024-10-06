from faker import Faker
from random import choice
import csv

fake = Faker('en_US')

def student_record(rows):
  student_response = []

  class_response = ['SS1', 'SS2', 'SS3']
  gender = ['Female', 'Male']
  age = ['12-14', '15-17', '18 and above']
  school = ['Public', 'Private']
  residence = ['Urban', 'Rural']
  school_distance = ['<1km', '1-2km', '>2km']
  family_type = ['Nuclear', 'Polygamous']
  school_has_library = ['Yes','No']
  library_visit = ['Daily','Weekly','Monthly','Rarely','Never']
  access_to_computer_lab = ['Yes','No']
  extra_mural_class = ['Yes','No']
  class_participation = ['Low', 'Moderate', 'High']
  extra_curricular_activities = ['Yes', 'No']
  extra_curricular_participation = ['Sports','Debate/Quiz clubs','Science/Math clubs','None']
  hours_on_curricular_activities = ['1–3 hours','4–6 hours','7 hours or more','None']
  hours_spent_studying = ['Less than 1 hour','1–2 hours','3–4 hours','5 hours or more']
  stressed = ['Yes', 'No']
  confidence_in_passing_exam = ['Very confident','Somewhat confident','Not confident']
  prepare_exam_with_online_resources = ['Yes','No']
  challenge_preparing_for_exam = ['Lack of focus', 'time management','The fear of the unknown',
                                  'Lack of proper preparation','Lack of funds', 'lack of standard social amenity'
                                  ]

  for _ in range(rows):
    data = {
      'class': choice(class_response),
      'gender': choice(gender),
      'age': choice(age),
      'school': choice(school),
      'residence': choice(residence),
      'school_distance': choice(school_distance),
      'family_type': choice(family_type),
      'school_has_library': choice(school_has_library),
      'library_visit': choice(library_visit),
      'access_to_computer_lab': choice(access_to_computer_lab),
      'extra_mural_class': choice(extra_mural_class),
      'class_participation': choice(class_participation),
      'extra_curricular_activities': choice(extra_curricular_activities),
      'extra_curricular_participation': choice(extra_curricular_participation),
      'hours_on_curricular_activities': choice(hours_on_curricular_activities),
      'hours_spent_studying': choice(hours_spent_studying),
      'stressed': choice(stressed),
      'confidence_in_passing_exam': choice(confidence_in_passing_exam),
      'prepare_exam_with_online_resources': choice(prepare_exam_with_online_resources),
      'challenge_preparing_for_exam': choice(challenge_preparing_for_exam)



    }

    student_response.append(data)
  
  return student_response


def save_as_csv(data, filename):
  with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

records = 100
student_record__= student_record(records)
save_as_csv(student_record__, './student_record.csv')