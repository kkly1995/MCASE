# MCASE
 
Monte Carlo with ASE (MCASE) uses the facilities of [ASE](https://wiki.fysik.dtu.dk/ase/) to do classical and path-integral Monte Carlo for statistical mechanics. A general overview of the method and algorithm can be found in the `background` directory. This code was designed specifically for [this project](https://doi.org/10.48550/arXiv.2409.19484) on atomic hydrogen; however, it is possible to use it for other things. The code is agnostic to the type of model used (so long as it can be used as an ASE calculator) or the types of particles in the simulation (so long as they can be read in the XYZ format), but the methods used here are more amenable to a monatomic system, e.g. only one step size can be specified. This was a personal code, and for posterity, all of its oddities and imperfections have been kept intact, no cleanup has been done.

To "install," simply add the `mcase` directory to your `PYTHONPATH`. The main simulation scripts are in `bin`, which can also be added to your `PATH` for execution. Only numpy, scipy, and ASE are strictly required. Specific ASE calculators will also require their own installation. For example, one obviously cannot use a MACE calculator without first installing [MACE](https://github.com/ACEsuit/mace).

The different types of simulations that can be done by MCASE are separated into different scripts. Here is a brief description of the main scripts:
- `mcase_nvt`: Classical NVT, the base algorithm using just the ASE calculator
- `mcase_table_nvt`: Classical NVT, using an ASE calculator plus a tabulated pair potential
- `mcase_npt`: Classical NPT, using just the ASE calculator
- `mcase_table_npt`: Classical NPT, using an ASE calculator plus a tabulated pair potential
- `mcase_cubic_npt`: Classical NPT, the cell is fixed to always be cubic with length L, which is allowed to vary
- `mcase_table_cubic_npt`: Same as `mcase_cubic_npt`, using an ASE calculator plus a tabulated pair potential
- `pimcase_table_nvt`: Path integral version of `mcase_table_nvt`
- `pimcase_table_npt`: Path integral version of `mcase_table_npt`
- `pimcase_table_cubic_npt`: Path integral version of `mcase_table_cubic_npt`

# Usage

Assuming you have `bin` added to your `PATH`, a simulation can be performed just by calling
```
pimcase_table_npt input
```
where `input` contains key-value pairs specifying the simulation parameters. The name of the input file is arbitrary, it just needs to be passed into the script.
An example input file looks like
```
xyz		walker.xyz
calculator	mace
model		../../../../hydrogen.model
table		/home/ly1/H/table/HH.table
temperature	250
pressure	500
timestep	0.0006
cellstep	0.06
samples		4000
save_slice	samples.xyz
save_every	100
save_xyz	walker.xyz
```
More generically:
```
xyz		[string, name of XYZ file to read in. for PIMC, must have multiple configurations, and this will form the path]
calculator	[string, type of ASE calculator. current options are: nep, dp, nequip, mace]
model		[string, name of file to read in as the ASE calculator]
table		[string, name of file to read in as tabulated pair potential. needs to be in LAMMPS table form]
temperature	[float, desired temperature in kelvin]
pressure	[float, desired pressure in GPa. not used in NVT]
timestep	[float, specifies the step size of the all-particle move. this is tau in equation 2 in the background]
cellstep	[float, specifies the step size of the cell move. this is sigma_l in equation 4 in the background]
anglestep [float, sigma_a in equation 4 in the background. only used in the classical scripts mcase_npt and mcase_table_npt]
samples		[integer, number of samples to compute. one sample is one full loop through every degree of freedom]
save_slice	[string, only used in PIMC. name of file to save samples to. only slice 0 of the path is written]
save_every	[integer, specifies number of samples to compute before writing out configurations]
save_xyz	[string. in PIMC, specifies where the final configurations will be written, includes whole path. in classical scripts, serves same purpose as save_slice]
```
The reading of the ASE calculator via `calculator` and `model` is very simple but crude, and you will almost certainly need to modify the scripts to fit your needs.

In addition to writing out the configurations of samples, the scripts will print out the energy of each sample, as well as the cell parameters, where applicable. For example, `pimcase_table_npt` prints 5 numbers per sample: the "spring" energy (the first term of equation 7 in `background/main.pdf`), the potential energy as determined by the specified model, and the 3 cell lengths. A script like `mcase_nvt` only prints out one number per sample, the potential energy.
