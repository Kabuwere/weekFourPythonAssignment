class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def describe(self):
        return f"This is a {self.brand} {self.model} with {self.storage}GB storage."

# Subclass for Gaming Smartphones
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)
        self.cooling_system = cooling_system

    def gaming_feature(self):
        return f"{self.model} has a {self.cooling_system} cooling system for smooth gaming!"

# Subclass for Camera Smartphones
class CameraPhone(Smartphone):
    def __init__(self, brand, model, storage, camera_resolution):
        super().__init__(brand, model, storage)
        self.camera_resolution = camera_resolution

    def camera_feature(self):
        return f"{self.model} has a {self.camera_resolution}MP camera for high-quality photos!"

# Creating phone objects
phone1 = Smartphone("Samsung", "Galaxy S21", 128)
gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, "Liquid Cooling")
camera_phone = CameraPhone("Google", "Pixel 7 Pro", 128, 50)

print(phone1.describe())  
print(gaming_phone.gaming_feature())  
print(camera_phone.camera_feature())  
