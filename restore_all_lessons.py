#!/usr/bin/env python3

import os
import textwrap

BASE = os.path.expanduser("~/NOVA/lessons")


LESSONS = {

# ============================================================
# MATHEMATICS FORM 1
# ============================================================

"mathematics/form1/numbers.txt": """
MATHEMATICS — FORM 1
TOPIC: NUMBERS

Numbers are used to describe quantities and values.

Main ideas:
• Natural numbers
• Whole numbers
• Integers
• Positive and negative numbers
• Place value
• Ordering numbers
• Basic operations

Examples:

25 + 17 = 42
50 - 18 = 32
6 × 7 = 42
48 ÷ 6 = 8

Order of operations:
BODMAS means:
Brackets, Orders, Division, Multiplication,
Addition and Subtraction.

Example:
6 + 2 × 3
= 6 + 6
= 12

PRACTICE

1. Calculate 35 + 48.
2. Calculate 91 - 37.
3. Calculate 8 × 9.
4. Calculate 72 ÷ 8.
5. Evaluate 10 + 4 × 2.
""",

"mathematics/form1/fractions.txt": """
MATHEMATICS — FORM 1
TOPIC: FRACTIONS

A fraction represents part of a whole.

A fraction has:
• Numerator — the top number.
• Denominator — the bottom number.

Example:

3/5

3 is the numerator.
5 is the denominator.

Equivalent fractions:

1/2 = 2/4 = 3/6

Adding fractions with the same denominator:

2/7 + 3/7 = 5/7

For different denominators, find a common denominator.

Example:

1/2 + 1/4
= 2/4 + 1/4
= 3/4

PRACTICE

1. Simplify 6/12.
2. Calculate 2/5 + 1/5.
3. Calculate 3/4 - 1/4.
4. Convert 1 1/2 to an improper fraction.
""",

"mathematics/form1/algebra.txt": """
MATHEMATICS — FORM 1
TOPIC: ALGEBRA

Algebra uses letters and symbols to represent unknown values.

Example:

x + 5 = 12

Subtract 5 from both sides:

x = 7

Terms:
• Variable
• Constant
• Coefficient
• Expression
• Equation

Example:

3x + 4

3 is the coefficient.
x is the variable.
4 is the constant.

PRACTICE

1. Solve x + 8 = 15.
2. Solve x - 4 = 9.
3. Solve 2x = 18.
4. Simplify 3x + 2x.
""",

"mathematics/form1/geometry.txt": """
MATHEMATICS — FORM 1
TOPIC: GEOMETRY

Geometry deals with shapes, lines, angles and measurements.

Common shapes:
• Triangle
• Square
• Rectangle
• Circle

Important terms:
• Point
• Line
• Angle
• Parallel lines
• Perpendicular lines

A right angle is 90 degrees.

A straight angle is 180 degrees.

A complete turn is 360 degrees.

Rectangle perimeter:

P = 2(length + width)

Rectangle area:

A = length × width

PRACTICE

1. Find the perimeter of a rectangle 8 cm by 5 cm.
2. Find its area.
3. What is a right angle?
4. How many degrees are in a full turn?
""",

"mathematics/form1/statistics.txt": """
MATHEMATICS — FORM 1
TOPIC: STATISTICS

Statistics involves collecting, organizing and interpreting data.

Important terms:

Mean:
Mean = sum of values ÷ number of values.

Median:
The middle value after arranging data.

Mode:
The value occurring most often.

Range:
Largest value - smallest value.

Example:

2, 4, 4, 6, 9

Mean = 25 ÷ 5 = 5
Mode = 4
Median = 4
Range = 9 - 2 = 7

PRACTICE

Find the mean, median, mode and range of:

3, 5, 5, 7, 10
""",


# ============================================================
# MATHEMATICS FORM 2
# ============================================================

"mathematics/form2/indices.txt": """
MATHEMATICS — FORM 2
TOPIC: INDICES

An index represents repeated multiplication.

2³ = 2 × 2 × 2 = 8

Important laws:

aᵐ × aⁿ = aᵐ⁺ⁿ

aᵐ ÷ aⁿ = aᵐ⁻ⁿ

(aᵐ)ⁿ = aᵐⁿ

a⁰ = 1, where a is not zero.

Example:

2³ × 2²
= 2⁵
= 32

PRACTICE

1. Simplify 3² × 3³.
2. Simplify 5⁶ ÷ 5².
3. Evaluate 10⁰.
4. Evaluate 2⁴.
""",

"mathematics/form2/logarithms.txt": """
MATHEMATICS — FORM 2
TOPIC: LOGARITHMS

A logarithm is another way of expressing an index.

If:

2³ = 8

then:

log₂ 8 = 3

The base is 2.
The answer is 3.

Important relationship:

aˣ = y

means:

logₐ y = x

PRACTICE

1. Write 3² = 9 as a logarithm.
2. Find log₂ 16.
3. Find log₁₀ 100.
""",

"mathematics/form2/trigonometry.txt": """
MATHEMATICS — FORM 2
TOPIC: TRIGONOMETRY

Trigonometry studies relationships between angles
and sides of triangles.

For a right-angled triangle:

sin θ = opposite / hypotenuse

cos θ = adjacent / hypotenuse

tan θ = opposite / adjacent

A useful memory aid is SOH-CAH-TOA.

PRACTICE

1. State the meaning of SOH.
2. State the meaning of CAH.
3. State the meaning of TOA.
4. Identify the hypotenuse in a right triangle.
""",

"mathematics/form2/vectors.txt": """
MATHEMATICS — FORM 2
TOPIC: VECTORS

A vector has both magnitude and direction.

A scalar has magnitude only.

Examples of vectors:
• Displacement
• Velocity
• Force

Examples of scalars:
• Distance
• Speed
• Mass
• Time

Vectors can be represented using arrows.

PRACTICE

1. Define a vector.
2. Define a scalar.
3. Give two examples of each.
""",


# ============================================================
# MATHEMATICS FORM 3
# ============================================================

"mathematics/form3/quadratic_equations.txt": """
MATHEMATICS — FORM 3
TOPIC: QUADRATIC EQUATIONS

A quadratic equation commonly has the form:

ax² + bx + c = 0

where a is not zero.

Example:

x² - 5x + 6 = 0

Factorize:

(x - 2)(x - 3) = 0

Therefore:

x = 2 or x = 3

The quadratic formula is:

x = (-b ± √(b² - 4ac)) / 2a

PRACTICE

Solve:

1. x² - 7x + 12 = 0
2. x² - 9 = 0
3. x² + 5x + 6 = 0
""",

"mathematics/form3/matrices.txt": """
MATHEMATICS — FORM 3
TOPIC: MATRICES

A matrix is a rectangular arrangement of numbers.

Example:

[1  2]
[3  4]

This is a 2 × 2 matrix.

Matrices can be added when their dimensions are the same.

PRACTICE

Given:

A = [1 2]
    [3 4]

B = [5 6]
    [7 8]

Find A + B.
""",

"mathematics/form3/functions.txt": """
MATHEMATICS — FORM 3
TOPIC: FUNCTIONS

A function describes a relationship between input
and output values.

Example:

f(x) = 2x + 3

When x = 4:

f(4) = 2(4) + 3
     = 11

PRACTICE

For f(x) = 3x - 2:

1. Find f(2).
2. Find f(5).
3. Find f(10).
""",

"mathematics/form3/probability.txt": """
MATHEMATICS — FORM 3
TOPIC: PROBABILITY

Probability measures how likely an event is to occur.

Probability:

P(event) =
number of favourable outcomes /
total number of possible outcomes

Probability lies between 0 and 1.

Example:

A fair coin has two possible outcomes.

P(head) = 1/2.

PRACTICE

1. What is the probability of rolling a 6 on a fair die?
2. What is the probability of getting heads on a fair coin?
""",


# ============================================================
# MATHEMATICS FORM 4
# ============================================================

"mathematics/form4/calculus.txt": """
MATHEMATICS — FORM 4
TOPIC: CALCULUS

Calculus studies change and accumulation.

Two major branches are:

1. Differentiation
2. Integration

Differentiation is commonly used to find rates of change.

Integration can be used to find accumulated quantities
and areas.

Example:

If:

y = x²

then:

dy/dx = 2x

PRACTICE

Differentiate:

1. y = x³
2. y = 5x²
3. y = 7x
""",

"mathematics/form4/differentiation.txt": """
MATHEMATICS — FORM 4
TOPIC: DIFFERENTIATION

Differentiation measures how a quantity changes.

Power rule:

d/dx(xⁿ) = nxⁿ⁻¹

Example:

y = x⁴

dy/dx = 4x³

Another example:

y = 3x²

dy/dx = 6x

PRACTICE

Differentiate:

1. x⁵
2. 4x³
3. 8x²
4. 6x
""",

"mathematics/form4/integration.txt": """
MATHEMATICS — FORM 4
TOPIC: INTEGRATION

Integration is the reverse process of differentiation.

Power rule:

∫xⁿ dx = xⁿ⁺¹/(n+1) + C

Example:

∫x² dx = x³/3 + C

C represents the constant of integration.

PRACTICE

Integrate:

1. x²
2. 3x²
3. 4x³
""",

"mathematics/form4/linear_programming.txt": """
MATHEMATICS — FORM 4
TOPIC: LINEAR PROGRAMMING

Linear programming is used to find the best solution
under given constraints.

Common terms:
• Objective function
• Constraints
• Feasible region
• Maximum
• Minimum

Problems can be represented using inequalities
and graphs.

PRACTICE

Explain:
1. Objective function.
2. Constraint.
3. Feasible region.
""",


# ============================================================
# ENGLISH FORM 4
# ============================================================

"english/form4/kcse_revision.txt": """
ENGLISH — FORM 4
KCSE REVISION

Important areas include:

1. Grammar
2. Comprehension
3. Functional writing
4. Oral skills
5. Literary analysis
6. Summary writing

Grammar revision should include:
• Parts of speech
• Sentence structure
• Tenses
• Agreement
• Reported speech
• Active and passive voice

Functional writing may include:
• Formal letters
• Informal letters
• Reports
• Speeches
• Articles
• Notices

PRACTICE

Write a short formal letter requesting information
from a school administration.
""",

"english/form4/set_book.txt": """
ENGLISH — FORM 4
SET BOOK

When studying a set book, examine:

• Plot
• Characters
• Themes
• Setting
• Conflict
• Style
• Literary devices
• Important events
• Lessons

For every major character, identify:
1. Character traits.
2. Important actions.
3. Relationships.
4. Contribution to the story.

PRACTICE

Choose a character from your current set book
and explain three important character traits.
""",


# ============================================================
# KISWAHILI FORM 1
# ============================================================

"kiswahili/form1/sarufi.txt": """
KISWAHILI — FORM 1
MADA: SARUFI

Sarufi ni kanuni zinazotawala matumizi sahihi ya lugha.

Vipengele vya msingi:

• Nomino
• Vitenzi
• Vivumishi
• Viwakilishi
• Vielezi
• Viunganishi

Mfano:

Mtoto anasoma kitabu.

Mtoto ni nomino.
Anasoma ni kitenzi.
Kitabu ni nomino.

MAZOEZI

1. Taja nomino mbili.
2. Taja vitenzi viwili.
3. Tunga sentensi ukitumia kivumishi.
""",


# ============================================================
# BIOLOGY
# ============================================================

"biology/form1/introduction.txt": """
BIOLOGY — INTRODUCTION

Biology is the study of living organisms.

Major branches include:
• Botany
• Zoology
• Microbiology
• Ecology

Characteristics of living organisms can be remembered
using MRS GREN:

Movement
Respiration
Sensitivity
Growth
Reproduction
Excretion
Nutrition

PRACTICE

1. Define biology.
2. List five characteristics of living organisms.
3. Give two branches of biology.
""",

"biology/form1/cell.txt": """
BIOLOGY — THE CELL

The cell is the basic structural and functional unit
of living organisms.

Major cell structures include:

• Cell membrane
• Cytoplasm
• Nucleus
• Mitochondria
• Ribosomes

Plant cells also commonly have:
• Cell wall
• Chloroplasts
• Large vacuole

PRACTICE

1. What is a cell?
2. State two differences between plant and animal cells.
3. State the function of the nucleus.
""",

"biology/form2/nutrition.txt": """
BIOLOGY — NUTRITION

Nutrition is the process by which organisms obtain
and use nutrients.

Major nutrients include:
• Carbohydrates
• Proteins
• Fats
• Vitamins
• Minerals
• Water

A balanced diet contains appropriate amounts
of different nutrients.

PRACTICE

1. Name three nutrients.
2. State the importance of proteins.
3. What is a balanced diet?
""",

"biology/form3/reproduction.txt": """
BIOLOGY — REPRODUCTION

Reproduction is the process by which organisms
produce new organisms.

Two broad types are:

• Asexual reproduction
• Sexual reproduction

Asexual reproduction involves one parent
and usually produces genetically similar offspring.

Sexual reproduction involves the fusion of
male and female gametes.

PRACTICE

1. Define reproduction.
2. Compare sexual and asexual reproduction.
""",

"biology/form4/ecology.txt": """
BIOLOGY — ECOLOGY

Ecology is the study of relationships between organisms
and their environment.

Important terms:
• Habitat
• Population
• Community
• Ecosystem
• Food chain
• Food web

Example food chain:

Grass → grasshopper → frog → snake

Energy flows through ecosystems.

PRACTICE

1. Define ecosystem.
2. Construct a simple food chain.
3. Explain the difference between a habitat and population.
""",


# ============================================================
# CHEMISTRY
# ============================================================

"chemistry/form1/introduction.txt": """
CHEMISTRY — INTRODUCTION

Chemistry is the study of matter and the changes
that matter undergoes.

Matter exists mainly as:

• Solids
• Liquids
• Gases

Examples:

Solid — stone
Liquid — water
Gas — oxygen

PRACTICE

1. Define chemistry.
2. Name the three common states of matter.
3. Give one example of each.
""",

"chemistry/form1/atoms.txt": """
CHEMISTRY — ATOMS

An atom is the smallest unit of an element
that retains the chemical properties of that element.

Main subatomic particles:

• Proton — positive
• Neutron — neutral
• Electron — negative

Protons and neutrons are found in the nucleus.
Electrons occupy regions around the nucleus.

PRACTICE

1. Name the three subatomic particles.
2. State their charges.
""",

"chemistry/form2/acids_bases.txt": """
CHEMISTRY — ACIDS AND BASES

Acids and bases have different chemical properties.

Examples of acids:
• Hydrochloric acid
• Sulfuric acid
• Ethanoic acid

Examples of bases:
• Sodium hydroxide
• Calcium hydroxide

The pH scale is commonly used to describe acidity
and alkalinity.

PRACTICE

1. Give two examples of acids.
2. Give two examples of bases.
3. What does pH measure?
""",

"chemistry/form3/chemical_reactions.txt": """
CHEMISTRY — CHEMICAL REACTIONS

A chemical reaction changes reactants into products.

Example:

Hydrogen + oxygen → water

Signs of chemical reactions may include:
• Colour change
• Gas production
• Temperature change
• Formation of a precipitate

PRACTICE

1. Define reactant.
2. Define product.
3. Give two signs of a chemical reaction.
""",

"chemistry/form4/organic_chemistry.txt": """
CHEMISTRY — ORGANIC CHEMISTRY

Organic chemistry studies carbon-containing compounds.

Important groups include:

• Alkanes
• Alkenes
• Alkynes
• Alcohols
• Carboxylic acids

Hydrocarbons contain carbon and hydrogen.

PRACTICE

1. What is organic chemistry?
2. Define hydrocarbon.
3. Name two classes of hydrocarbons.
""",


# ============================================================
# PHYSICS
# ============================================================

"physics/form1/introduction.txt": """
PHYSICS — INTRODUCTION

Physics studies matter, energy, motion and forces.

Major areas include:
• Mechanics
• Heat
• Light
• Sound
• Electricity
• Magnetism

Measurements use standard units.

Examples:
Length — metre
Time — second
Mass — kilogram

PRACTICE

1. Define physics.
2. Name three areas of physics.
""",

"physics/form2/force.txt": """
PHYSICS — FORCE

A force is a push or pull that can change
the motion or shape of an object.

The SI unit of force is the newton (N).

Force can cause:
• Acceleration
• Deceleration
• Change of direction
• Deformation

PRACTICE

1. Define force.
2. State its SI unit.
3. Give two effects of force.
""",

"physics/form3/motion.txt": """
PHYSICS — MOTION

Motion describes a change in position with time.

Speed:

speed = distance / time

Velocity includes direction.

Acceleration:

acceleration =
change in velocity / time

PRACTICE

1. A car travels 100 m in 20 s. Find its speed.
2. Define velocity.
3. Define acceleration.
""",

"physics/form4/electricity.txt": """
PHYSICS — ELECTRICITY

Electric current is the flow of electric charge.

Important quantities:

Current — measured in amperes (A)
Voltage — measured in volts (V)
Resistance — measured in ohms (Ω)

Ohm's law:

V = IR

where:
V = voltage
I = current
R = resistance

PRACTICE

1. State Ohm's law.
2. If V = 12 V and R = 4 Ω, find I.
""",


# ============================================================
# GEOGRAPHY
# ============================================================

"geography/form1/introduction.txt": """
GEOGRAPHY — INTRODUCTION

Geography studies places, people, environments
and relationships between them.

Main branches:

• Physical geography
• Human geography

Physical geography studies natural features
such as rivers, mountains and climate.

Human geography studies people and their activities.

PRACTICE

1. Define geography.
2. Name the two major branches.
""",

"geography/form2/weather.txt": """
GEOGRAPHY — WEATHER

Weather is the condition of the atmosphere
at a particular place and time.

Elements include:
• Temperature
• Rainfall
• Wind
• Humidity
• Air pressure
• Sunshine

Weather differs from climate.
Climate describes average atmospheric conditions
over a long period.

PRACTICE

1. Define weather.
2. List four elements of weather.
3. Differentiate weather and climate.
""",

"geography/form3/agriculture.txt": """
GEOGRAPHY — AGRICULTURE

Agriculture involves cultivation of crops
and rearing of animals.

Factors affecting agriculture include:
• Climate
• Soil
• Relief
• Markets
• Labour
• Technology

Agriculture can provide food, employment
and raw materials.

PRACTICE

1. Define agriculture.
2. List four factors affecting agriculture.
""",

"geography/form4/environment.txt": """
GEOGRAPHY — ENVIRONMENT

The environment includes living and non-living
components surrounding organisms.

Environmental problems include:
• Deforestation
• Soil erosion
• Pollution
• Climate change
• Loss of biodiversity

Conservation aims to protect natural resources.

PRACTICE

1. Define environment.
2. Name three environmental problems.
3. Give two conservation methods.
""",


# ============================================================
# HISTORY
# ============================================================

"history/form1/introduction.txt": """
HISTORY — INTRODUCTION

History is the study of past human events.

Sources of history include:

• Oral traditions
• Written records
• Archaeological evidence
• Linguistic evidence
• Anthropology

Historians use evidence to understand past societies.

PRACTICE

1. Define history.
2. List four sources of history.
""",

"history/form2/early_man.txt": """
HISTORY — EARLY HUMAN SOCIETIES

Early humans developed tools, learned to use fire
and developed different ways of obtaining food.

Archaeological evidence helps researchers understand
early human life.

Important developments included:
• Tool making
• Fire use
• Hunting
• Gathering
• Agriculture
• Settlement

PRACTICE

1. Name three developments associated with early humans.
2. Why is archaeology important?
""",

"history/form3/colonialism.txt": """
HISTORY — COLONIALISM

Colonialism involved political and economic control
of one territory by another power.

In Africa, colonial rule affected:
• Political systems
• Land ownership
• Economies
• Education
• Transport
• Social structures

African communities responded in different ways,
including resistance and adaptation.

PRACTICE

1. Define colonialism.
2. Name three effects of colonial rule.
3. Explain why some communities resisted.
""",

"history/form4/independence.txt": """
HISTORY — INDEPENDENCE

African independence movements sought self-government.

Factors that contributed to independence included:

• Nationalism
• Political organizations
• Education
• Economic changes
• International developments

Independence involved negotiations, political action
and, in some places, armed conflict.

PRACTICE

1. Define nationalism.
2. State three factors that contributed to independence.
""",


# ============================================================
# CRE
# ============================================================

"cre/form1/creation.txt": """
CRE — CREATION

The creation account in Genesis describes God
as the creator of the universe.

Important ideas include:
• Creation
• Human responsibility
• Stewardship
• Relationship between God and humanity

Human beings are expected to care for creation.

PRACTICE

1. What is stewardship?
2. Give two ways humans can care for the environment.
""",

"cre/form2/ten_commandments.txt": """
CRE — THE TEN COMMANDMENTS

The Ten Commandments provide important moral
and religious teachings.

They emphasize:
• Worship of God
• Respect
• Honesty
• Family
• Faithfulness
• Protection of life and property

PRACTICE

Explain two moral lessons that can be learned
from the commandments.
""",

"cre/form3/prophets.txt": """
CRE — PROPHETS

Prophets communicated God's messages to people.

Prophetic roles included:
• Teaching
• Warning
• Correcting injustice
• Encouraging faith
• Calling people to repentance

PRACTICE

1. Who is a prophet?
2. State three roles of prophets.
""",

"cre/form4/jesus_ministry.txt": """
CRE — THE MINISTRY OF JESUS

The ministry of Jesus included:
• Teaching
• Healing
• Parables
• Compassion
• Calling people to repentance
• Serving others

His teachings emphasized love, forgiveness,
faith and responsibility.

PRACTICE

1. Name three aspects of Jesus' ministry.
2. State two lessons from his teachings.
""",


# ============================================================
# BUSINESS
# ============================================================

"business/form1/introduction.txt": """
BUSINESS — INTRODUCTION

Business involves activities concerned with producing,
buying and selling goods and services.

Examples:
• Retailing
• Wholesaling
• Manufacturing
• Banking
• Transport

Business can satisfy human wants and create employment.

PRACTICE

1. Define business.
2. Name four types of business activity.
""",

"business/form2/entrepreneurship.txt": """
BUSINESS — ENTREPRENEURSHIP

An entrepreneur identifies opportunities
and organizes resources to start or operate
a business.

Important qualities include:
• Creativity
• Initiative
• Persistence
• Decision-making
• Responsibility

PRACTICE

1. Define entrepreneur.
2. List four entrepreneurial qualities.
""",

"business/form3/marketing.txt": """
BUSINESS — MARKETING

Marketing involves activities used to identify,
communicate and satisfy customer needs.

The marketing mix is commonly described as:

• Product
• Price
• Place
• Promotion

These are known as the 4Ps.

PRACTICE

1. Explain the 4Ps.
2. Why is promotion important?
""",

"business/form4/accounting.txt": """
BUSINESS — BASIC ACCOUNTING

Accounting involves recording, classifying
and summarizing financial transactions.

Basic terms:

Assets — things owned by a business.

Liabilities — amounts owed by a business.

Capital — owner's investment.

Revenue — income earned.

Expenses — costs incurred.

PRACTICE

Classify each as an asset, liability,
capital, revenue or expense:

1. Cash
2. Bank loan
3. Owner investment
4. Sales
5. Rent
""",


# ============================================================
# AGRICULTURE
# ============================================================

"agriculture/form1/introduction.txt": """
AGRICULTURE — INTRODUCTION

Agriculture involves crop production,
animal production and related activities.

Importance includes:
• Food production
• Employment
• Income
• Raw materials
• Trade

PRACTICE

1. Define agriculture.
2. State four importance of agriculture.
""",

"agriculture/form2/soil.txt": """
AGRICULTURE — SOIL

Soil supports plant growth.

Main components include:
• Mineral particles
• Organic matter
• Water
• Air
• Living organisms

Important soil properties include:
• Texture
• Structure
• Fertility
• Drainage

PRACTICE

1. Name four components of soil.
2. Define soil fertility.
""",

"agriculture/form3/crop_production.txt": """
AGRICULTURE — CROP PRODUCTION

Crop production involves preparing land,
planting, maintaining and harvesting crops.

Important practices include:
• Land preparation
• Seed selection
• Planting
• Weeding
• Pest control
• Harvesting
• Storage

PRACTICE

Arrange the main stages of crop production
in their correct order.
""",

"agriculture/form4/livestock.txt": """
AGRICULTURE — LIVESTOCK

Livestock farming involves keeping animals
for useful products and services.

Examples:
• Cattle
• Goats
• Sheep
• Poultry
• Pigs

Products include:
• Milk
• Meat
• Eggs
• Hides and skins

PRACTICE

1. Name four livestock animals.
2. State three livestock products.
""",


# ============================================================
# COMPUTER
# ============================================================

"computer/form1/introduction.txt": """
COMPUTER — INTRODUCTION

A computer is an electronic device that
processes data into information.

Basic operations include:

Input → Processing → Output → Storage

Examples of input devices:
• Keyboard
• Mouse
• Scanner

Output devices:
• Monitor
• Printer
• Speakers

PRACTICE

1. Define a computer.
2. Name three input devices.
3. Name three output devices.
""",

"computer/form2/hardware_software.txt": """
COMPUTER — HARDWARE AND SOFTWARE

Hardware refers to physical computer components.

Examples:
• CPU
• Keyboard
• Monitor
• Storage devices

Software refers to programs and instructions
used by computers.

Examples:
• Operating systems
• Applications
• Utilities

PRACTICE

Classify these as hardware or software:

1. Keyboard
2. Android
3. Monitor
4. Web browser
""",

"computer/form3/programming.txt": """
COMPUTER — PROGRAMMING

Programming is the process of creating instructions
that a computer can execute.

A program may use:
• Variables
• Conditions
• Loops
• Functions
• Data structures

Example idea:

IF temperature is greater than 30
THEN display "Hot"

PRACTICE

1. Define programming.
2. What is a variable?
3. What is a loop?
""",

"computer/form4/python.txt": """
COMPUTER — PYTHON PROGRAMMING

Python is a high-level programming language.

Example:

name = "NOVA"

print(name)

Variables store values.

Conditional example:

if age >= 18:
    print("Adult")

Loops can repeat instructions.

Example:

for number in range(5):
    print(number)

PRACTICE

1. Create a variable called name.
2. Print the variable.
3. Write a simple if statement.
""",

}


def create_lessons():
    created = 0

    for relative_path, content in LESSONS.items():

        path = os.path.join(
            BASE,
            relative_path
        )

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(
                textwrap.dedent(content).strip()
                + "\n"
            )

        print("CREATED:", relative_path)

        created += 1

    return created


def main():

    print()
    print("========================================")
    print("       NOVA FULL LESSON RESTORER")
    print("========================================")
    print()

    total = create_lessons()

    print()
    print("========================================")
    print("LESSON RESTORATION COMPLETE")
    print("Lessons created:", total)
    print("Location:", BASE)
    print("========================================")
    print()

    # Test important lessons
    tests = [
        "mathematics/form1/numbers.txt",
        "mathematics/form2/indices.txt",
        "mathematics/form3/quadratic_equations.txt",
        "mathematics/form4/calculus.txt",
        "english/form4/kcse_revision.txt",
        "kiswahili/form1/sarufi.txt",
        "biology/form1/cell.txt",
        "chemistry/form1/atoms.txt",
        "physics/form3/motion.txt",
        "geography/form2/weather.txt",
        "history/form3/colonialism.txt",
        "cre/form4/jesus_ministry.txt",
        "business/form3/marketing.txt",
        "agriculture/form2/soil.txt",
        "computer/form4/python.txt",
    ]

    print("VERIFYING LESSONS...")
    print()

    missing = []

    for lesson in tests:

        path = os.path.join(
            BASE,
            lesson
        )

        if os.path.isfile(path):
            print("OK:", lesson)
        else:
            print("MISSING:", lesson)
            missing.append(lesson)

    print()

    if missing:
        print(
            "WARNING:",
            len(missing),
            "test lessons are missing."
        )
    else:
        print("ALL TEST LESSONS: OK")

    print()
    print("You can now use:")
    print()
    print("cd ~/NOVA")
    print("python main.py")
    print()
    print("Example:")
    print("teach mathematics form1 numbers")
    print()
    print("========================================")


if __name__ == "__main__":
    main()
