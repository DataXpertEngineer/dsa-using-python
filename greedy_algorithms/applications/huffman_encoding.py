"""
Huffman Encoding

Variable-length prefix code for lossless data compression.

Problem Statement:
-------------------
Given characters and their frequencies, create binary codes such that:
1. More frequent characters have shorter codes
2. No code is prefix of another (prefix-free)
3. Total encoded length is minimized

Why Greedy?
-----------
- Greedy choice: Always merge two least frequent nodes
- Optimal substructure: Optimal tree contains optimal subtrees
- Creates optimal prefix code

Useful in:
- Data compression
- File compression (ZIP, GZIP)
- Common interview problems
"""

from typing import Dict, List, Tuple, Optional
import heapq


# ----------------------------------------------------------------------
# Huffman Node
# ----------------------------------------------------------------------
class HuffmanNode:
    """Node in Huffman tree."""
    
    def __init__(self, char: Optional[str] = None, freq: int = 0,
                 left: Optional['HuffmanNode'] = None,
                 right: Optional['HuffmanNode'] = None) -> None:
        """Initialize Huffman node."""
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other: 'HuffmanNode') -> bool:
        """Comparison for priority queue."""
        return self.freq < other.freq


# ----------------------------------------------------------------------
# Huffman Encoding (Language-agnostic, optimal)
# ----------------------------------------------------------------------
def build_huffman_tree(frequencies: Dict[str, int]) -> Optional[HuffmanNode]:
    """
    Build Huffman tree using greedy algorithm.

    Algorithm:
    1. Create leaf node for each character
    2. Use priority queue (min-heap)
    3. Repeatedly merge two nodes with lowest frequency
    4. Continue until one node remains

    Args:
        frequencies (Dict[str, int]): Character frequencies

    Returns:
        Optional[HuffmanNode]: Root of Huffman tree

    Complexity:
        Time: O(n log n)  - n characters, log n for heap operations.
        Space: O(n)      - Tree nodes.
    """
    if not frequencies:
        return None
    
    # Create leaf nodes
    heap: List[HuffmanNode] = []
    for char, freq in frequencies.items():
        heapq.heappush(heap, HuffmanNode(char, freq))
    
    # Build tree
    while len(heap) > 1:
        # Extract two nodes with minimum frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create internal node
        merged = HuffmanNode(
            char=None,
            freq=left.freq + right.freq,
            left=left,
            right=right
        )
        
        heapq.heappush(heap, merged)
    
    return heapq.heappop(heap)


# ----------------------------------------------------------------------
# Generate Huffman Codes
# ----------------------------------------------------------------------
def generate_codes(root: Optional[HuffmanNode]) -> Dict[str, str]:
    """
    Generate Huffman codes by traversing tree.

    Args:
        root (Optional[HuffmanNode]): Root of Huffman tree

    Returns:
        Dict[str, str]: Character to code mapping

    Complexity:
        Time: O(n)     - Traverse all nodes once.
        Space: O(n)   - Code storage + recursion stack.
    """
    codes: Dict[str, str] = {}
    
    def traverse(node: Optional[HuffmanNode], code: str) -> None:
        if node is None:
            return
        
        if node.char is not None:
            # Leaf node
            codes[node.char] = code if code else "0"
        else:
            # Internal node
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")
    
    traverse(root, "")
    return codes


# ----------------------------------------------------------------------
# Encode and Decode
# ----------------------------------------------------------------------
def huffman_encode(text: str, frequencies: Dict[str, int]) -> Tuple[str, Dict[str, str]]:
    """
    Encode text using Huffman coding.

    Args:
        text (str): Text to encode
        frequencies (Dict[str, int]): Character frequencies

    Returns:
        Tuple[str, Dict[str, str]]: Encoded string and code dictionary

    Complexity:
        Time: O(n log n)  - Build tree + encode.
        Space: O(n)       - Tree + codes.
    """
    tree = build_huffman_tree(frequencies)
    codes = generate_codes(tree)
    
    encoded = "".join(codes[char] for char in text)
    return encoded, codes


def huffman_decode(encoded: str, root: Optional[HuffmanNode]) -> str:
    """
    Decode Huffman encoded string.

    Args:
        encoded (str): Encoded binary string
        root (Optional[HuffmanNode]): Root of Huffman tree

    Returns:
        str: Decoded text

    Complexity:
        Time: O(m)     - m is length of encoded string.
        Space: O(1)   - Only uses variables.
    """
    if root is None:
        return ""
    
    decoded = []
    current = root
    
    for bit in encoded:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        
        if current.char is not None:
            decoded.append(current.char)
            current = root
    
    return "".join(decoded)


# ----------------------------------------------------------------------
# Example Usage
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("\n📌 Example: Huffman Encoding Demonstration")
    
    text = "hello world"
    frequencies = {}
    for char in text:
        frequencies[char] = frequencies.get(char, 0) + 1
    
    print(f"Text: {text}")
    print(f"Frequencies: {frequencies}")
    
    tree = build_huffman_tree(frequencies)
    codes = generate_codes(tree)
    
    print("\nHuffman Codes:")
    for char, code in sorted(codes.items()):
        print(f"  '{char}': {code}")
    
    encoded, _ = huffman_encode(text, frequencies)
    print(f"\nEncoded: {encoded}")
    print(f"Original length: {len(text) * 8} bits")
    print(f"Encoded length: {len(encoded)} bits")
    print(f"Compression ratio: {len(encoded) / (len(text) * 8):.2%}")
    
    decoded = huffman_decode(encoded, tree)
    print(f"Decoded: {decoded}")
    print(f"Match: {text == decoded}")

