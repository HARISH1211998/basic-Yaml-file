def main():
    material_type_1 = ["leather", "rubber"]
    material_type_2 = ["lher", "rubb", 12]  # Note: This includes an integer
    material_type_3 = ["canvas", "rubber"]
    shoes_1 = create_shoes(material_type_1)
    shoes_2 = create_shoes(material_type_2)
    shoes_3 = create_shoes(material_type_3)
    shoes = [shoes_1, shoes_2, shoes_3]
    for shoe in shoes:
        if shoe['type'] == 'unknown':
            print(f"Unknown material list: {shoe['material_list']}")
        else:
            print(f"All values: {shoe['material_list']}")

def create_shoes(material_list):
    if 'leather' in material_list and 'rubber' in material_list:
        shoes = "boat"
    elif 'canvas' in material_list and 'rubber' in material_list:
        shoes = "sneaker"
    else:
        shoes = "unknown"
    return {'type': shoes, 'material_list': material_list}

if __name__ == '__main__':
    main()
