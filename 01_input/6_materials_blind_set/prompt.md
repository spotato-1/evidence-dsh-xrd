# Input Prompts

> Original benchmark input prompts. The working-directory path is replaced with `<working_directory>`.

## Amorphous

`<working_directory>` contains an XRD dataset; the composition is an amorphous carbon anode. Process the data strictly following the xrd plugin. Save the work under the data folder.

If the AI judges that a conventional refinement is not meaningful, choose the amorphous workflow. If, after that choice, the AI asks for information, use: "The synthesis route is a g-C3N4 hollow micro-rod coated with multiple layers of different materials, sintered at 1100 °C under Ar. TEM shows good carbonization, the hollow-rod morphology is retained, and the tube wall has three layers of carbon with different densities from the inside outward."

## Fe2O3_Fe3O4_2ph

`<working_directory>` contains an XRD dataset; the composition is a two-phase material of Fe2O3 + Fe3O4. Process the data strictly following the xrd plugin; the target is publication-level (R ≤ 10). Save the work under the data folder.

## FE50

`<working_directory>` contains an XRD dataset; it is a Prussian blue crystal with nominal formula KxFe0.5Mn0.5[Fe(CN)6], synthesized by ball-milling Fe4[Fe(CN)6]3, manganese oxide tetrahydrate, and potassium citrate in 50% ethanol/water. `<working_directory>` provides two similar-material CIF files as reference. The material should be considered to contain extensive defects, especially lattice distortion, vacancies, and split sites. Process strictly following the xrd plugin, force the complex-case checklist, strictly follow the planned workflow, and consider all defects and possible fitting changes. When in doubt, first consider the fitting approach and scientific self-consistency; before entering the final GSAS engine, all adjustments target lowering R. The target is publication-level (R ≤ 10) as far as possible. Save the work under the data folder.

## Fluoroapatite

`<working_directory>` contains an XRD dataset; the composition is a fluorapatite ore powder sample. Process the data strictly following the xrd plugin. Save the work under the data folder.

## LayeredOxide

`<working_directory>` contains an XRD dataset; it is a layered oxide crystal with nominal formula Na0.72Ni0.33Mn0.62Mo0.05O2 (feed ratio), raw materials NaOH, Na2MoO4·2H2O, Ni(CH3COO)2·4H2O, Mn(CH3COO)2·4H2O, citric acid; synthesis: sol-gel then ball milling, calcined at 450 °C for 5 h + 900 °C for 12 h. The material should be considered to contain some sodium molybdate impurity. Process the data strictly following the xrd plugin; the target is publication-level (R ≤ 10). Save the work under the data folder.

## LiFePO4

`<working_directory>` contains an XRD dataset; the composition is LiFePO4, and Li/Fe antisite defects should be considered. Process the data strictly following the xrd plugin, load the full complex-case checklist; the target is the lowest possible R. Save the work under the data folder.
