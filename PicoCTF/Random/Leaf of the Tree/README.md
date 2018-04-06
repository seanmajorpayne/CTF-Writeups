# PicoCTF 2017 - Level 1 - Leaf of the Tree

**Category:** Random **Points:** 20

**Description:**

> We found this annoyingly named directory tree starting at 
> /problems/4052472b84e355d1e1a42f5899fe0e76. It would be pretty lame to type out all 
> of those directory names but maybe there is something in there worth finding? And maybe
> we dont need to type out all those names...? Follow the trunk, using cat and ls!

The problem intends for us to solve this using tab completion, but there is a much easier
way. We can use the Linux find command to find all files under the current directory.

```
find . -type f
./trunk/branch04cf/leafd6ec
./trunk/branch04cf/leaf6b5f
./trunk/trunkef9b/trunk99e1/branch1a36/leaf33af
./trunk/trunkef9b/trunk99e1/trunk54f4/branch9b67/leafc6aa
./trunk/trunkef9b/trunk99e1/trunk54f4/branchb9e7/leafc50a
./trunk/trunkef9b/trunk99e1/trunk54f4/trunk61be/branch00bc/leaf9ced
./trunk/trunkef9b/trunk99e1/trunk54f4/trunk61be/branch00bc/leaf94f2
./trunk/trunkef9b/trunk99e1/trunk54f4/trunk61be/trunk89be/trunk87bf/
trunkb252/branchd8bd/leaf7420
./trunk/trunkef9b/trunk99e1/trunk54f4/trunk61be/trunk89be/trunk87bf/
trunkb252/flag
./trunk/trunkef9b/trunk99e1/trunk54f4/trunk61be/branchbe5f/leaf4304
./trunk/trunkef9b/trunk99e1/trunk54f4/trunk61be/branchbe5f/leaf351b
./trunk/trunkef9b/trunk99e1/branch6b01/leaf518f
./trunk/trunkef9b/trunk99e1/branch6b01/leaf2ee6
./trunk/trunkef9b/trunk99e1/branch6b01/leaf41c0
$ cat ./trunk/trunkef9b/trunk99e1/trunk54f4/trunk61be/trunk89be/trunk87bf/trunkb252/flag
aae8c400f845fd47fdbb6a77ba027771
```

