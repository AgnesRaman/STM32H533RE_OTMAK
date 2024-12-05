import yaml

# Baca file YAML
with open("schematic.yaml", "r") as file:
    data = yaml.safe_load(file)

# Konversi ke netlist format KiCad
netlist = []
netlist.append("(export (version D)")

# Tambahkan komponen
for component in data['components']:
    if component['type'] == 'driver IC':
        netlist.append(f"  (components (comp (ref U1) (value {component['name']}) (footprint Housings_DIP:DIP-8_W7.62mm))")
    elif component['type'] == 'capacitor':
        netlist.append(f"  (components (comp (ref C1) (value {component['value']}) (footprint Capacitors_SMD:C_0603))")
    elif component['type'] == 'N-channel MOSFET':
        if 'high' in component['name']:
            netlist.append(f"  (components (comp (ref Q1) (value {component['model']}) (footprint TO_SOT_Packages_SMD:SOT-223-3))")
        else:
            netlist.append(f"  (components (comp (ref Q2) (value {component['model']}) (footprint TO_SOT_Packages_SMD:SOT-223-3))")
    elif component['type'] == 'DC motor':
        netlist.append(f"  (components (comp (ref M1) (value {component['name']}) (footprint Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical))")

# Tambahkan koneksi
for component in data['components']:
    if 'connections' in component:
        for connection in component['connections']:
            netlist.append(f"  (net (code 1) (name {connection})")

netlist.append(")")
netlist = "\n".join(netlist)

# Tulis netlist ke file
with open("schematic.net", "w") as file:
    file.write(netlist)
