# [blib](../__init__.md)[\.cycles](__init__.md)[\.utils](utils.md)

**Source code:** [blib/cycles/utils\.py](../../../blib/cycles/utils.py)

Utility functions for the Cycles Blib package\.  

#### [Functions](#functions-1)
* <code>utils\.[**check\_asset**](#function-utils-check_asset)</code>
* <code>utils\.[**check\_file**](#function-utils-check_file)</code>
* <code>utils\.[**get\_sub\_type**](#function-utils-get_sub_type)</code>

## Functions
* <a id="function-utils-check_asset"></a>*function* utils\.**check\_asset(**<i>asset, do\_raise=False</i>**)**  
    Check if asset is a Cycles material or node group,  
    and thus is exportable by the 'cycles' package\.  

    **Arguments:**
    * <code>**asset** \(*any* *type*\)</code>: Asset to be checked for validity\.
    * <code>**do\_raise** \(*bool*\)</code>: If True, an exception is raised for invalid assets,
        instead of returning False\.

    **Returns:**

    <code>**bool**</code>: True if check is passed, otherwise returns False\.  
    Note that False is only ever returned if 'do\_raise' is False,  
    otherwise an exception is raised instead\.  

    **Raises:**
    * <code>**blib\.exeptions\.InvalidObject**</code>: If the check fails and 'do\_raise' is True\.


---

* <a id="function-utils-check_file"></a>*function* utils\.**check\_file(**<i>f\_path, sub=None</i>**)**  
    Check if file is a 'cycles' type blib file\.  
    Optionally check if file is of a specific subtype\.  

    **Arguments:**
    * <code>**f\_path** \(*str*\)</code>: Path to the file to be checked\.
    * <code>**sub** \(*str* or *None*\)</code>: If a str is provided, it should be the subtype to check against,
        if None is given, no subtype check is performed\.

    **Returns:**

    <code>**bool**</code>: True if the file is of type 'cycles', and if it matches the optional subtype\.  


---

* <a id="function-utils-get_sub_type"></a>*function* utils\.**get\_sub\_type(**<i>f\_path</i>**)**  
    Get the subtype of a 'cycles' type Blib file\.  

    **Arguments:**
    * <code>**f\_path** \(*str*\)</code>: Path to the file to be checked\.

    **Returns:**

    <code>**str**</code> or <code>**None**</code>  
    A string containing the Blib sub\-type is returned,  
    if no valid sub\-type is found, None is returned\.  

