def advanced_rent_calculator(base_rent, 
                             lease_length, 
                             utilities_included=False, 
                             estimated_utilities=0, 
                             maintenance_fees=0, 
                             repairs_upkeep=0, 
                             security_deposit=0, 
                             pet_rent=0, 
                             pet_deposit=0, 
                             renters_insurance=0, 
                             landlord_insurance=0, 
                             annual_rent_increase=0, 
                             parking_fees=0, 
                             laundry_fees=0, 
                             trash_recycling_fees=0,
                             late_payment_fee=0, 
                             months_late=0):
    
    total_base_rent = base_rent * lease_length

  
    total_utilities = 0
    if not utilities_included:
        total_utilities = estimated_utilities * lease_length

    
    total_additional_fees = (maintenance_fees + pet_rent + parking_fees + laundry_fees + trash_recycling_fees) * lease_length

    
    total_fixed_costs = security_deposit + pet_deposit + (renters_insurance * lease_length) + (landlord_insurance * lease_length)


    increased_rent = 0
    if annual_rent_increase > 0 and lease_length > 12:
        num_increases = lease_length // 12
        for i in range(1, num_increases + 1):
            increased_rent += (base_rent * annual_rent_increase / 100) * (lease_length - (i * 12))

    total_late_fees = late_payment_fee * months_late

    total_rent = (total_base_rent + total_utilities + total_additional_fees + 
                  total_fixed_costs + increased_rent + total_late_fees)

    return total_rent

def get_user_input():
    base_rent = float(input("Enter the base rent per month: "))
    lease_length = int(input("Enter the lease length in months: "))
    
    utilities_included = input("Are utilities included (yes/no)? ").strip().lower() == 'yes'
    if not utilities_included:
        estimated_utilities = float(input("Enter the estimated monthly utility cost: "))
    else:
        estimated_utilities = 0
    
    maintenance_fees = float(input("Enter the monthly maintenance fees: "))
    repairs_upkeep = float(input("Enter the estimated monthly repair/upkeep costs (if any): "))
    security_deposit = float(input("Enter the security deposit: "))
    
    pet_rent = float(input("Enter the pet rent per month (if applicable): "))
    pet_deposit = float(input("Enter the pet deposit (if applicable): "))
    
    renters_insurance = float(input("Enter the monthly renter's insurance: "))
    landlord_insurance = float(input("Enter the monthly landlord's insurance: "))
    
    annual_rent_increase = float(input("Enter the annual rent increase percentage: "))
    
    parking_fees = float(input("Enter the monthly parking fees (if applicable): "))
    laundry_fees = float(input("Enter the monthly laundry fees (if applicable): "))
    trash_recycling_fees = float(input("Enter the monthly trash/recycling fees (if applicable): "))
    
    late_payment_fee = float(input("Enter the late payment fee (if applicable): "))
    months_late = int(input("Enter the number of months late (if applicable): "))
    
    total_rent = advanced_rent_calculator(
        base_rent=base_rent,
        lease_length=lease_length,
        utilities_included=utilities_included,
        estimated_utilities=estimated_utilities,
        maintenance_fees=maintenance_fees,
        repairs_upkeep=repairs_upkeep,
        security_deposit=security_deposit,
        pet_rent=pet_rent,
        pet_deposit=pet_deposit,
        renters_insurance=renters_insurance,
        landlord_insurance=landlord_insurance,
        annual_rent_increase=annual_rent_increase,
        parking_fees=parking_fees,
        laundry_fees=laundry_fees,
        trash_recycling_fees=trash_recycling_fees,
        late_payment_fee=late_payment_fee,
        months_late=months_late
    )
    
    print(f"Total Rent for the Lease: ${total_rent:.2f}")


get_user_input()
