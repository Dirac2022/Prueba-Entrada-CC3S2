class Question:
    """Esta clase representa una pregunta de Trivia con sus opciones
    de respuesta y la respuesta correcta.
    """
    def __init__(self, question_text: str, answer_options: list, correct_answer: int):
        """Crea una instancia de la clase Question

        Args:
            question_text (str): La pregunta a mostrar
            answer_options (list): Las opciones de respuesta
            correct_answer (int): La respuesta correcta (índice de la opción correcta)
        """
        self._question_text = question_text
        self._answer_options = answer_options
        self._correct_answer = correct_answer
        
    
    def show_question(self) -> int:
        """Muestra la pregunta y sus opciones de respuesta por consola
        y solicita la respuesta del participante

        Returns:
            int: La posición en la lista 'answer_options' de la respuesta seleccionada por el usuario.
            Al valor ingresado se le resta 1 para que concuerde con los indices de la lista 'answer_options'
        """
        print(self._question_text)
        for i, option in enumerate(self._answer_options):
            print(f"{i + 1}) {option}")
        answer = int(input("Tu respuesta: "))
        return answer - 1  # Restar 1 para que el índice comience en 0
    
            
    def check_answer(self, user_answer: int) -> bool:
        """Verifica si la respuesta es correcta

        Args:
            user_answer (int): El número de la opcion elegida por el usuario.

        Returns:
            bool: True si la respuesta del participante coincide con 'correct_answer'
        """
        return user_answer == self._correct_answer
    