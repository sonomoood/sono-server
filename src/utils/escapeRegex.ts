const escapeRegex = (string : String) => {
    return string
        .replace(/[|\\{}()[\]^$+*?.]/g, '\\$&')
        .replace(/-/g, '\\x2d');
  };
  
  export default escapeRegex;