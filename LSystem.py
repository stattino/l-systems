import re
import sys
import numpy as np
import matplotlib.pyplot as plt


class LSystem:
    def __init__(self, systemtype, axiom, rules, starting_angle=0, angle_increment=0):
        self.systemtype = systemtype
        self.axiom = axiom
        self.rules = rules
        self.state = axiom
        self.state_list = [char for char in self.axiom]
        self.is_used = [0 for char in self.axiom]
        self.gen = 0
        self.angle = np.deg2rad(starting_angle)
        self.angle_increment = np.deg2rad(angle_increment)
        self.coordinates = np.zeros((1, 2))

    def test_system(self):
        self.print_system()
        self.print_result()
        self.next_generation()
        self.print_result()
        self.next_generation()
        self.print_result()

    def print_system(self):
        print("This is a {0} with axiom '{1}' and the rules {2}".format(self.systemtype, self.axiom, self.rules))

    def print_result(self):
        print("Current state: {0} after {1} generations".format(self.state, self.gen))

    def age_system(self, n_gens):
        for i in range(n_gens):
            self.next_generation()

    def refresh_state_list(self):
        self.state_list = [char for char in self.state]

    def refresh_is_used_list(self):
        self.is_used = [0 for i in self.state]

    def next_generation(self):
        for rule in self.rules:
            self.perform_rule(rule)
        self.state = "".join(self.state_list)
        self.gen += 1
        self.refresh_is_used_list()
        self.refresh_state_list()
        self.print_result()
        return

    def perform_rule(self, rule):
        lhs, rhs = re.split("=", rule)
        for i in range(len(self.state_list)):
            if self.state_list[i] == lhs and self.is_used[i] == 0:
                del self.state_list[i]
                self.state_list.insert(i, rhs)
                self.is_used[i] = 1

    def print_coordinates(self):
        print("Coordinates {0} with angle {1}".format(self.coordinates, self.angle))

    def create_coordinates(self):
        self.coordinates = np.zeros((1, 2))
        for i in self.state:
            if i == "+":
                self.angle += self.angle_increment
                continue
            elif i == "-":
                self.angle -= self.angle_increment
                continue
            elif i in ("X", "Y"):
                continue
            last_coordinate = self.coordinates[-1, :]
            this_move = np.array([np.sin(self.angle), np.cos(self.angle)], dtype=float)
            new_point = np.array([np.add(last_coordinate, this_move)], dtype=float)
            self.coordinates = np.append(self.coordinates, new_point, axis=0)

    def easy_plot(self):
        plt.figure()
        self.create_coordinates()
        plt.plot(self.coordinates[:, 0], self.coordinates[:, 1])
        plt.axis('equal')
