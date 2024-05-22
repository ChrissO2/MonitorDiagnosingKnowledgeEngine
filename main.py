from experta import *
from problem_descriptions import ProblemDescription
from facts import Problem, Solution
from knowledge_engine import MonitorDiagnosis


def main():
    """CLI for diagnosing monitor problems."""
    engine = MonitorDiagnosis()
    while True:
        print("Podaj opis problemu z monitorem:")
        for idx, problem in enumerate(ProblemDescription, 1):
            print(f"{idx}. {problem.value}")
        print('0. wyjście')

        user_input = input('> ')
        if user_input == '0':
            break
        try:
            user_input = int(user_input)
        except ValueError:
            print('Podaj poprawną wartość', end='\n\n')
            continue
        if user_input < 1 or user_input > len(ProblemDescription):
            print('Podaj poprawną wartość', end='\n\n')
            continue

        problem_description = list(ProblemDescription)[user_input - 1].value

        print('Czy kabel zasilający jest podłączony?')
        is_cable_connected = input('t/n: ')
        is_cable_connected = is_cable_connected.lower() == 't'

        print('Czy monitor jest włączony?')
        is_monitor_on = input('t/n: ')
        is_monitor_on = is_monitor_on.lower() == 't'

        print('Czy komputer jest w trybie uśpienia?')
        is_sleep_mode_active = input('t/n: ')
        is_sleep_mode_active = is_sleep_mode_active.lower() == 't'

        engine.reset()
        engine.declare(Problem(description=problem_description,
                               is_cable_connected=is_cable_connected,
                               is_monitor_on=is_monitor_on,
                               is_sleep_mode_active=is_sleep_mode_active))

        engine.run()
        solutions = []
        for fact in engine.facts.values():
            if isinstance(fact, Solution):
                solutions.append(fact["step"])
        print('\n\nRozwiązanie problemu:')
        for solution in solutions:
            print(solution)
        print('\n\n')


if __name__ == '__main__':
    main()
