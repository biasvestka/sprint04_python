import kivy
import os



class BikeInfoApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical")

        self.model_input = TextInput(hint_text="Modelo da Bicicleta")
        self.serial_input = TextInput(hint_text="Número de Série")
        self.owner_input = TextInput(hint_text="Proprietário")

        self.submit_button = Button(text="Salvar Informações")
        self.submit_button.bind(on_press=self.save_to_json)

        self.show_bikes_button = Button(text="Ver Bicicletas")
        self.show_bikes_button.bind(on_press=self.show_bikes)

        self.layout.add_widget(Label(text="Digite as informações da bicicleta:"))
        self.layout.add_widget(self.model_input)
        self.layout.add_widget(self.serial_input)
        self.layout.add_widget(self.owner_input)
        self.layout.add_widget(self.submit_button)
        self.layout.add_widget(self.show_bikes_button)

        return self.layout

    def save_to_json(self, instance):
        bike_info = {
            "modelo": self.model_input.text,
            "numero_serie": self.serial_input.text,
            "proprietario": self.owner_input.text
        }

        # Verificar a existência do arquivo JSON (bikes.json)
        if os.path.exists("bikes.json"):
            # Ler o JSON existente (bikes.json)
            with open("bikes.json", "r") as json_file:
                data = json.load(json_file)
        else:
            # Se o arquivo não existir, crie uma lista vazia
            data = []

        # Adicionar as novas informações ao dicionário
        data.append(bike_info)

        # Escrever de volta ao JSON (bikes.json)
        with open("bikes.json", "w") as json_file:
            json.dump(data, json_file)

        # Limpar os campos de entrada após a adição das informações
        self.model_input.text = ""
        self.serial_input.text = ""
        self.owner_input.text = ""

        # Imprimir o conteúdo do arquivo JSON para verificação
        with open("bikes.json", "r") as json_file:
            print(json.load(json_file))

    def show_bikes(self, instance):
        if os.path.exists("bikes.json"):
            with open("bikes.json", "r") as json_file:
                bike_data = json.load(json_file)

            if not bike_data:
                print("Nenhuma bicicleta cadastrada.")
            else:
                for bike in bike_data:
                    print("Modelo:", bike["modelo"])
                    print("Número de Série:", bike["numero_serie"])
                    print("Proprietário:", bike["proprietario"])
                    print("\n")
        else:
            print("Nenhuma bicicleta cadastrada.")




if __name__ == "__main__":
    BikeInfoApp().run()
