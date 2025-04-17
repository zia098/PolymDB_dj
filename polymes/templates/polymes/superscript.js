/**
 * Converts caret notation (e.g., 10^6) to Unicode superscripts (e.g., 10⁶)
 * For display in the PolymDB application
 */
document.addEventListener('DOMContentLoaded', function() {
  // Find all elements that might contain caret notation
  // Added strong, th, and a elements to catch polymerase names in tables and links
  const elements = document.querySelectorAll('.property-item div, pre, p, span, td, strong, th, a, h1, h2, h3, h4, h5');
  
  // Mapping of regular characters to their Unicode superscript equivalents
  const superscriptMap = {
    // Numbers
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', 
    '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
    
    // Symbols
    '+': '⁺', '-': '⁻', '=': '⁼', '(': '⁽', ')': '⁾',
    
    // Lowercase letters
    'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ', 
    'f': 'ᶠ', 'g': 'ᵍ', 'h': 'ʰ', 'i': 'ⁱ', 'j': 'ʲ',
    'k': 'ᵏ', 'l': 'ˡ', 'm': 'ᵐ', 'n': 'ⁿ', 'o': 'ᵒ',
    'p': 'ᵖ', 'r': 'ʳ', 's': 'ˢ', 't': 'ᵗ', 'u': 'ᵘ',
    'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ', 'y': 'ʸ', 'z': 'ᶻ',
    
    // Uppercase letters (limited availability in Unicode)
    'A': 'ᴬ', 'B': 'ᴮ', 'D': 'ᴰ', 'E': 'ᴱ', 'G': 'ᴳ',
    'H': 'ᴴ', 'I': 'ᴵ', 'J': 'ᴶ', 'K': 'ᴷ', 'L': 'ᴸ',
    'M': 'ᴹ', 'N': 'ᴺ', 'O': 'ᴼ', 'P': 'ᴾ', 'R': 'ᴿ',
    'T': 'ᵀ', 'U': 'ᵁ', 'V': 'ⱽ', 'W': 'ᵂ'
  };
  
  elements.forEach(function(element) {
    // Get the current HTML content
    let html = element.innerHTML;
    
    // Use regex to find patterns like "anything^anything"
    // Updated pattern to better handle complex cases
    html = html.replace(/(\S+)\^(\S+)/g, function(match, base, exp) {
      let superscript = '';
      
      // Convert each character in the exponent to its superscript equivalent if available
      for (let i = 0; i < exp.length; i++) {
        const char = exp[i];
        
        if (superscriptMap[char]) {
          // Use Unicode superscript if available
          superscript += superscriptMap[char];
        } else if (char.toUpperCase() === char && /[A-Z]/.test(char)) {
          // For uppercase letters without Unicode superscripts, use HTML tags
          superscript += '<sup>' + char + '</sup>';
        } else {
          // For any other characters without superscript versions
          superscript += char;
        }
      }
      
      return base + superscript;
    });
    
    // Update the element with the converted content
    element.innerHTML = html;
  });
});
