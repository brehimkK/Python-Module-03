#!/usr/bin/env python3

import sys

def find_max(all_input: dict) -> str:
    max_val = None 
    name_max = ""
    for name, value in all_input.items():
        if max_val is None or value >= max_val:
            max_val = value
            name_max = name
    return f"{name_max} ({max_val} units)"

def fin_min(all_input: dict) -> str:
    min_val = None 
    min_name = ""
    for name, value in all_input.items():
        if min_val is None or value < min_val:
            min_val = value
            min_name = name
    return f"{min_name} ({min_val} unit)"

def input_to_dic()->tuple:
    all_inputs = {}
    total = 0
    for a in sys.argv[1:]:
        name, quantity = a.split(':')
        quantity_nb = int(quantity)
        all_inputs[name] = quantity_nb
        total = total + quantity_nb
    return all_inputs, total 

def current_in(all_inputs: dict,total : int )->None:
    printed = {}
    for i in range(len(all_inputs)):
        max_v = -1
        max_k = ""
        for key, value in all_inputs.items():
            if key not in printed and value > max_v:
                max_v = value
                max_k = key
        
        # Avoid division by zero if total is 0
        percentage = (max_v / total * 100) if total > 0 else 0
        print(f"{max_k}: {max_v} units ({percentage:.1f}%)")
        printed[max_k] = max_v
def item_categories(all_inputs)->None:
    Moderate = {}
    Scarc = {}
    for name, value in all_inputs.items():
        if value >= 5:
            Moderate.update({name: value})
        else:
            Scarc.update({name: value})
    print(f"Moderate: {Moderate}")
    print(f"Scarce: {Scarc}")
    
def main() -> None:
    if len(sys.argv) < 2:
        return
    all_inputs, total  = input_to_dic()

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(all_inputs)}")

    print("\n=== Current Inventory ===")
    current_in(all_inputs,total)
    
    print("\n=== Inventory Statistics ===")
    max_str = find_max(all_inputs)
    
    print(f"Most abundant: {max_str}")
    min_str = fin_min(all_inputs)
    print(f"Least abundant: {min_str}")

    print("\n=== Item Categories ===")
    item_categories(all_inputs)
    print("\n=== Management Suggestions ===")
    actual_min = None
    for v in all_inputs.values():
        if actual_min is None or v < actual_min:
            actual_min = v

    restock = ""
    for name, value in all_inputs.items():
        if value == actual_min:
            if restock == "":
                restock = name
            else:
                restock = restock + ", " + name
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    # Formatting keys/values without join() and using authorized methods
    d_keys = ""
    for k in all_inputs.keys():
        d_keys += (", " if d_keys != "" else "") + k
    
    d_vals = ""
    for v in all_inputs.values():
        d_vals += (", " if d_vals != "" else "") + str(v)

    print(f"Dictionary keys: {d_keys}")
    print(f"Dictionary values: {d_vals}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in all_inputs}")

if __name__ == "__main__":
    main()
