def forecast(forecast_list, current_time):
    lap = False
    new_fore_list = []
    for day in forecast_list:
        for element in day["hour"]:
            fore_time = element["time"].split(" ")
            new_current_time = current_time.split(" ")

            current_hour = new_current_time[1].split(":")[0]

            if len(current_hour) == 1:
                current_hour = f"0{current_hour}"

            fore_hour = fore_time[1].split(":")[0]

            if not lap and current_hour == fore_hour:
                lap = True
            elif lap and current_hour == fore_hour:
                break

            if lap:
                new_fore_list.append(element)
    
    return new_fore_list

def air_quality(aiq_data):
    air_status = "N/A"
    
    #Convertir Dic en list
    aiq_data = [(key, value) for key, value in aiq_data.items()][0:7]
    air_obj = aiq_data[6][1]
    aiq_data = aiq_data[:6]
    air_high = 0
    
    air_high = max(aiq_data, key=lambda x: x[1])
    
    if air_obj == 1:
        air_status = ["green", "Air quality is good. Perfect for outdoor activities."]
    elif air_obj == 2:
        air_status = ["yellow", "Moderate air quality. Caution for sensitive individuals."]
    elif air_obj == 3 or air_obj == 4:
        air_status = ["orange", "Poor air quality. Limit outdoor exposure."]
    elif air_obj == 5 or air_obj == 6:
        air_status = ["red", "Very poor air quality. Avoid outdoor activities, especially for those with respiratory conditions."]

    return [air_status, air_high, aiq_data]