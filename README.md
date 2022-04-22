# project3
This THE is about the automation of the application of the Turkish inheritance law.
In the Turkish legal system, the priority group (PG) system is used for determining the legal heirship to a deceased1 (D); a PG consists of a set of heirs H = {h1,...,hn}. If spouse(D), the spouse of the deceased (D), is alive, the inheritance (I) will be shared between spouse(D) and one of the PGs. If, on the other hand, spouse(D) is not alive, the whole inheritance, I, belongs
to one of the PGs.
There are some rules in the PG system:
R1. In order for the inheritance (in whole or in part) to pass from the current PG to the next PG, there must be no heir in the current PG (meaning also no descendants of those in that PG exist or are alive).
R2. The shares of the “first” heirs H in each PG are equal. In other words, denoting the shares of an heir hi by s(hi), the shares satisfy the following rule: s(h1) = ... = s(hn).
R3. Theshareofadepartedheir,s(hi),inaPGpassestohis/herdescendants(descendants(hi)2 – also called “second” heirs), shared by them equally.
The list of PGs and their order for getting inheritance are defined as follows:
First PG heirs are the children of the deceased D. If spouse(D) is alive, heirs in this PG share among themselves the three-quarters (3/4) of the inheritance I. In this inheritance process, if a child hi has departed then his/her descendants will partake his/her share s(hi) (R3).
Second PG heirs are the parents of the deceased D. In order for an individual in the second PG to become an heir, there must be no single individual (alive) in the first PG (R1). If spouse(D) is alive, heirs in this PG share among themselves a half (1/2) of the inheritance I. In case of a departed mother or father, their descendants partake among themselves the share of the departed mother or father (R3). In other words, the siblings of the deceased can also be the heirs in the second PG.
1Although the word ‘deceased’ is a synonym for words such as ‘departed’, and ‘dead’, for the sake of clarity, we will use ‘deceased’ only for the person whose inheritance is being distributed.
2A person p is a member of descendants(hi) iff. hi = parent(parent(...(parent(p))...)), where parent can be either father or mother; i.e. there is a bloodline from hi to p in the family tree.
 
Third PG heirs are the grandparents of the deceased D. In other words, the heirs of the third PG are the grandmothers and the grandfathers. In order for the people in this group to be heirs, there must be no individual (alive) in the first or second PG (R1). If spouse(D) is alive, heirs in this PG share among themselves a quarter (1/4) of the inheritance I. If a grandparent hi has departed then his/her descendants partake the share s(hi) (R3).
Inheritance Status of the Alive Spouse (spouse(D)) depends with which PG he/she is heir:
• If he/she is heir with the first PG then he/she gets (1/4) of the inheritance I.
• If he/she is heir with the second PG then he/she gets (1/2) of the inheritance I. • If he/she is heir with the third PG then he/she gets (3/4) of the inheritance I. • If no heir is found in all three PGs, spouse(D) receives the entire inheritance.
If spouse(D) is not alive, in contrary to the individuals of PGs, the descendants of the spouse do not become heirs.
How the descendants partake a share s(x) for a person x depends on the closeness to x and whether other descendants are alive or not.
1. Assume that x has share s(x).
2. Calculate the immediate partakers:
P = {c|c∈children(x) ∧
(alive(c)=True ∨ (alive(c)=False∧alivedescendants(c)̸=∅))}
3. Each member of P has an equal share; i.e. s(p) = s(x)/|P | for each p ∈ P .
4. For each c ∈ children(x), if alive(c) = False and alive descendants(c) ̸= ∅, then
repeat Steps 1-4 with x ← c and s(c).
See Figure 1 for three examples.
    𝑎𝑎𝑎
𝑏𝑐𝑑𝑏𝑐𝑑𝑏𝑐𝑑
𝑒𝑓𝑒𝑓𝑒𝑓
        If heir 𝑎 has departed and has share 𝑠(𝑎) = 𝑥, then:
𝑠 𝑏 =𝑠 𝑐 =𝑠(𝑑)=𝑥3
(a)
If heir 𝑎 has departed and has share 𝑠(𝑎) = 𝑥, then:
𝑠 𝑐 =𝑠(𝑑)=𝑥2
(b)
If heir 𝑎 has departed and has share 𝑠(𝑎) = 𝑥, then:
𝑠 𝑏 =𝑠 𝑐 =𝑠(𝑑)=𝑥3 since 𝑐 has departed, 𝑐’s share is
shared by 𝑐′s descendants:
𝑠𝑒 =𝑠𝑓 = 𝑥/3 2
(c)
Figure 1: Three example scenarios for how descendants partake a share. A ribbon signifies a deceased/departed person.

YOUR TASK
• Writeafunctionnamedinheritance(Descriptions),whichisprovidedasinputDescriptions, a partial and unordered information about the members of the family.
• The input of the function, Descriptions, has the following format: [Description_String_1, Description_String_2, ..., Description_String_N],
where each Description_String_i can be any of the following:
– "CHILD mother_name father_name child_1_name child_2_name . . . child_n_name",
– "MARRIED individual_1_name individual_2_name",
– "DEPARTED individual_name",
– "DECEASED individual_name inheritance_value".
Each individual’s name (.._name), a lowercase word containing only letters from the En- glish alphabet (no spaces) and underscores, is unique throughout the whole family. Words in a description string are separated by one or more blanks.
• The return value of the function is a single Python list, which consists of tuples of the form: ("individual_name", inheritance_share_value),
where inheritance_share_value is a floating point number. The ordering of the tuples is unimportant.
