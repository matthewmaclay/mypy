import csv
import os


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        if body_whl:
            self.body_length, self.body_width, self.body_height = [float(x) for x in body_whl.split(
                'x')]
        else:
            self.body_length, self.body_width, self.body_height = [
                0.0, 0.0, 0.0]

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row[0] == 'car':
                    car_list.append(
                        Car(row[0], row[1], row[3], row[5], row[2]))
                elif row[0] == 'truck':
                    car_list.append(
                        Truck(row[0], row[1], row[3], row[5], row[4]))
                elif row[0] == 'spec_machine':
                    car_list.append(
                        SpecMachine(row[0], row[1], row[3], row[5], row[6]))
            except IndexError:
                pass
    return car_list
