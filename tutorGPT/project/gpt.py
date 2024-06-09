from openai import OpenAI
# import keys
import os
client = OpenAI(api_key=os.getenv("gpt_key"))

MODEL = "gpt-3.5-turbo"

def get_questions_from_notes(notes):
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role":"system","content":"You are a helpful assistant that makes multiple choice questions given notes."},
            {"role":"assistant","content":"Desired output format:\nQuestion|question_text|1|option_text|2|option_text|3|option_text|4|option_text|Answer|correct_option_number"},
            {"role":"assistant", "content":"Do not output question numbers or anything other than the desired output. Also make sure that none of the individual promts have | so as to not confuse things. The only separation between different questions should be '\\n'. This is important for processing, must be like a csv file. You may search the internet for questions related to the notes. Use the internet to fact-check your generated questions, and ensure that the questions you generate have accurate answers."},
            {"role":"assistant", 'content':'If you are given thermochemistry notes, an example output containing two questions is: \n"Question|Which unit is equivalent to the energy needed to raise the temperature of 1.00 gram of water by 1.00o C?|1|Calorie|2|Joule|3|Kilowatt-hour|4|British Thermal Unit|Answer|1\nQuestion|Which kind of reaction involves the release of heat to the surroundings?|1|Endothermic|2|Isoschist|3|Exothermic|4|Isothermal|Answer|3"'},
            {"role":"assistant","content":"Given these notes, please generate 20 questions in the desired output format: "+notes}

        ]
    )
    return completion.choices[0].message.content

# print(get_questions_from_notes('''



# Chapter 17: Thermochemistry

# 17.1: The Flow of Energy
# 17.2: Measuring and Expressing Enthalpy Changes
# 17.3: Heat in Changes of State
# 17.4 Calculating Heats of Reaction


# Energy Transformations
# Thermochemistry is the study of energy changes that occur during chemical reactions
# chemical bonds represent chemical potential energy
# stored energy
# heat represents the energy transferred into or out of chemical bonds
# Q is used to represent heat




# Etotal=       KE                     +                       PE                +  Q
# Energytotal=Kinetic Energy + Potential Energy + Heat
# 		motion			position	         transfer

# state function: Etotal=Efinal-Einitial=0 J (bc conservation of energy law)

# molecules are two or more atoms bonded together = potential energy bc the way the atoms are positioned close together
# when going through the air, molecule can move:
# rotationally
# translationally
# vibrationally

# rub hands = collisions between particles of skin generate heat
# blister = too much rubbing

# air around fire heats up → density decreases → air moves up

# System vs Surroundings
# The “system” is defined by the observer
# the “surrounding” is everything that is NOT in the system
# heat transfers into or out of the system MUST obey the conservation of energy law


# Measurement Units for Heat
# Calorie
# the energy needed to raise the temperature of 1.00 gram of water by 1.00o C
# 1 Calorie = 1 kilocalorie = 1,000 calories
# Joule
# 1 cal = 4.184 J
# Other units
# kW-hr (kilo Watt - Hour)
# ex: electricity costs
# BTU (British Thermal Unit)
# Horse Power (Power of one horse)
# ex: car motors
# eV (electron Volt)
# ex: used in electricity associated with atoms
# charge of electron x 1 volt

# For food:
# (uppercase C) Calorie: 1000x a regular energy calorie

# Heat Capacity
# the amount of energy needed to raise the temperature of an object by exactly 1.00oC

# Specific Heat
# the amount of energy needed to raise the temperature of 1.00 g of a substance exactly 1.00oC


# Observe the value of water in calories -- does it look familiar?

# Compare the values of ice to water to steam -- why do cities near oceans have moderate climates?

# Compare air (1.00 J/goC) to water -- why do deserts get so cold at night

# facts
# nonmetals have lower specific heat capacities than metals!
# high conductivity due to sea of electrons
# solids = fixed positions, so if heat hits one particle, they hit the next particle almost immediately (while with liquids, it’s more random).
# water = particles move together, harder to transmit signals
# gases = particles are much further apart from each other, random hitting of particles -- still sometimes collide
# cities near water sources have very fixed temperatures
# clouds act as blankets → heat radiated from earth get caught in it and it less cold

# Determining Specific Heat of Materials
# The specific heat is defined by
# Csp=QmT
# Q is the heat in Joules
# m is the mass of the system
# T is the change in temperature
# T=Tf-Ti

# Find heat capacity:
# CspmT=Q


# Calorimetry
# The controlled measurement of energy transferred into or out of a system
# Qsys=H=-Qsurr= -mCT
# Q is the heat in Joules
# H is the change in Enthalpy
# the energy released or absorbed by the chemical reaction
# m is the mass of the system
# C is the specific heat of the system
# T is the temperature final - temperature initial
# T=Tf-Ti
# Q=mCT
# Q is the heat in Joules
# m is the mass of the system
# C is the specific heat of the system
# T is the temperature final - temperature initial

# Practice Problems:
# How much heat is added to 150 mL of water with an initial temperature of 20.0oC and a final temperature of 45oC?
# mH2O=150 g
# TiH2O=20.0oC
# TfH2O=45.oC
# CH2O=4.184 JgoC
# Q=mCT=(150g)(4.184 JgoC)(45oC-20.0oC)=15.690 J=16kJ
# What is the final temperature when a 150. g block of copper at 250.oC is added to 455 mL of water at 18oC? Assume no heat is lost to the surroundings.
# -QCu=+QH2O
# TfCu=TfH2O
# (-1)QCu=mCuCcu(TfCu-TiCu)
# ↓
# QCu=mCuCcu(TiCu-TfCu)
# QH2O=mH2OCH2O(TfH2O-TiH2O)
# mCuCCu(-Tf+TiCu)=mH2OCH2O(Tf-TiH2O)
# 		↓
# Tf=mCuCCuTiCu+mH2OCH2OTiH2OmH2O+mCuCCu
# 		↓
# Tf==24.8oC

# Thermochemical equations
# The energy associated with a chemical reaction is called the heat of reaction
# Hrxn
# When a chemical reaction is written, the heat of reaction is included in the equation:
# When the energy is on the product side, the reaction is exothermic
# When the energy is on the reactant side, the reaction is endothermic
# The energy term in a reaction is treated like a coefficient and must be adjusted to accommodate different amounts of reactants
# example problem
# How much heat is released into the universe when 14 grams of oxygen reacts with excess hydrogen?
# 2H2(g)+O2(g)<=>2H2O(g)+486.6 kJ
# molO2=14 g329 g/mol=0.438 mol
# O2Hrxn=1486.6kJ=0.438x, x=213 kJ

# Exothermic Reaction
# 2H2 (g) + O2 (g) ⇐⇒ 2H2O (g) + 486.6 kJ

# Endothermic Reaction
# 2 C (s) + 2 H2 (g) + 52.4 kJ ⇐⇒ C2H4 (g)


# HELPFUL REFERENCE TABLES:
# chemistry-reference-tables-2011.pdf (nysed.gov)


# Heats of Combustion
# the heat of combustion is the same thing as the heat of reaction but it relates to a combustion reaction.
# Why is octane the preferred hydrocarbon for gasoline?
# Why do children get so animated after eating sugar?

# CH4 (g) + 2O2 (g) ⇐⇒CO2 (g)+ 2H2O (g)+890.4kJ

# If use larger hydrocarbons, it might solidify easier bc freezing point is higher.

# Energy Changes during melting/freezing and boiling/condensation
# the heat of fusion represents the amount of energy needed to change 1 gram of a substance from solid to liquid or the reverse
# the heat of vaporization is the same but for boiling and condensation
# distance between the particles represents potential energy

# How to convert kJ/mol to kJ/gram:
# 6.01 kJ1 mol1 mol18 g=334 Jg
# 	    ^
#          molar mass


# Enthalpy Implications
# melting and boiling are endothermic processes
# freezing and condensation are exothermic processes

# Heating/Cooling Curve of Water
# This curve shows the temperature changes of water as energy is added to the water
# What is happening when the slope is positive?
# What is happening when the slope is “0”?





# 								     ^
# 							just adds to potential energy
# 						(increasing the distance between molecules)

# Heating/Cooling Curve of Water
# Using the curve for water (or any material), the amount of energy needed to increase or decrease the temperature can be determined
# QT=?
# How much energy is required to increase the temperature of 100 g of ice from -10oC up to 110oC
# Q1=mCiceT=(100 g)(2.1JgoC)(0oC-(-10oC))=2100J
# Q2=mHf=(100 g)(6.01kJmol)=(100 g)(.334 Jg)=334J
# Q3=mCliqT=(100 g)(4.18JgoC)(100oC)=41800J
# Q4=mHv=(100 g)(40.07kJmol)=(100 g)(2.22 Jg)=222
# Q5=mCgasT=(100 g)(1.9JgoC)(10oC)=(100g)(2261Jg)=226100J
# 		QT=Q1+Q2+Q3+Q4+Q5=295 kJ
# ?????????????????????????????????????????????????????????????????

# Practice Problem
# How much energy is required to increase the temperature of 100g of water from 10oC up to 110oC?
# Q10->100=(100g)(4.18JgoC)(90oC)=37,620 J
# Qvap=(100g)(2261Jg)=226,100 J
# Q100->110=(100g)(1.9JgoC)(10oC)=1,900 J
# 					-----------
# 				Qtotal=265,620 J=266 kJ
# -----------------------------------------------------------------------------------------------------------
# MISSED STUFF, NEED TO GET NOTES FROM ANOTHER PERSON
# ______________________________________________________________

# Heat of Solution
# Hsoln
# The energy released or absorbed by a chemical dissolving in a solvent.
# NH4NO3 (s) + 25.7 kJ/mol ←→ NH4+ (aq) + NO3- (aq)
# 			   H2O

# NH4NO3 (s) + H2O (l) + 25.7 kJ/mol → NH4OH (aq) + HNO3 (aq)
# ^ don’t have to include the water tho, its simpler to just not include bc we already know

# Hess’ Law
# combine multiple reaction steps into a net reaction to find the heat of reaction for an intermediate step

# cross outs = catalysts
# doesn’t get created or destroyed in net reaction



# Hess’ Law

# Question:

# Answer:


# 2. 
# 2CO2+3H2O->C2H5OH+3O2  (875)
# 2C+2O2->2CO2  (-789.02)
# 3H2+3/2 O2->3H2O (-857.4)
# Overall = -771.42 kJ/mol


# Standard Heats of Formation
# Mathematically combine the heats of formation for each reactant and product
# Ho=Hfo(products)-Hfo(reactants)
# 		^			^
# 	             sum 			sum
# All elements
# standard heat of formation is 0.

# ionic compounds
# Hard to decompose
# standard heat of formation is very low

# Practice Problems:
# 2H2 (g) + O2 (g) ←→ 2H2O
#    0           0                  -242
# Ho=Hfo(products)-Hfo(reactants)
# Ho= -2422-(02+0)= -484 kJ/mol

# -----

# Mathematically combine the heats of formation for each reactant and product

# 2C (s) + 2 O2 (g) ←→ 2CO (g) + O2 (g)

# CO is catalyst






# What is the heat of formation when hydrogen gas is combined with oxygen gas?
# 2H2 (g) + O2 (g) → 2H2O (g)
#     0          0                -241.818
# -241.8182-(20+0)
# = -483.636
# What is the Hrxn when aqueous hydrochloric acid is mixed with solid sodium hydroxide?

# HCl (aq) + NaOH (s) → H2O (l) + NaCl (aq)
# -167.159   -425.609   -285.830   –410.9
# -410.9-285.830-(-167.159-425.609)= -103.962

# Enthalpy
# Represents the energy associated with that chemical reaction. This is often expressed as the Hxyz, where “xyz” signifies the specific energy term.

# Hxyz
# Hfus (fusion)
# Hvap (vaporization)
# Hfo (
# Hsolutiono
# Hsubo (sublimation)
# Hcombo (combustion)


# ''').split("\n"))