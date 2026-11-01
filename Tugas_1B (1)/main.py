from node import Node
from tree import Tree

tree = Tree()

tree.root = Node("R001", "Rektor")

tree.insert_node("R001", "WR1", "Wakil Rektor I")
tree.insert_node("R001", "WR2", "Wakil Rektor II")
tree.insert_node("R001", "WR3", "Wakil Rektor III")
tree.insert_node("R001", "D001", "Dekan FST")

print("Anak dari Rektor: ")
for child in tree.root.children:
    print(child.jabatan)


dekan = tree.search_id(tree.root, "D001")

tree.insert_node("D001", "WD1", "Wakil Dekan I")
tree.insert_node("D001", "WD2", "Wakil Dekan II")
tree.insert_node("D001", "WD3", "Wakil Dekan III")
tree.insert_node("D001", "KP001", "Ketua Prodi TIF")

print("\nAnak dari Dekan: ")
for child in dekan.children:
    print(child.jabatan)


kaprodi = tree.search_id(tree.root, "KP001")

tree.insert_node("KP001", "SP001", "Sekretaris Prodi")
tree.insert_node("KP001", "LAB001", "Kepala Laboratorium Komputer")
tree.insert_node("KP001", "KD001", "Koordinator Dosen")

print("\nAnak dari Kaprodi: ")
for child in kaprodi.children:
    print(child.jabatan)


labor = tree.search_id(tree.root, "LAB001")

tree.insert_node("LAB001", "AL001", "Asisten Laboratorium")
tree.insert_node("LAB001", "TL001", "Teknisi Laboratorium")

print("\nAnak dari Laboratorium: ")
for child in labor.children:
    print(child.jabatan)


koord_dosen = tree.search_id(tree.root, "KD001")

tree.insert_node("KD001", "DPA001", "Dosen Pembimbing Akademik")
tree.insert_node("KD001", "DPM001", "Dosen Pengampu Mata Kuliah")

print("\nAnak dari Koordinator Dosen: ")
for child in koord_dosen.children:
    print(child.jabatan)


hasil = tree.search_node(tree.root, "Teknisi Laboratorium")

if hasil is not None:
    print("\nData ditemukan!!")
    print(f"ID      : ", hasil.id)
    print(f"Jabatan : ", hasil.jabatan)

else:
    print("\nData tidak ditemukan")


print("\nPre-Order: ")
tree.preorder(tree.root)

print("\nIn-order: ")
tree.inorder(tree.root)

print("\nPost-Order: ")
tree.postorder(tree.root)


# OPERASI TRAVERSAL PADA STRUKTUR ORGANISASI YANG BARU
tree_dosen = Tree()

tree_dosen.root = Node("R001", "Rektor")

# Anak Rektor
tree_dosen.insert_node("R001", "SU001", "Senat Universitas")
tree_dosen.insert_node("R001", "WR1", "Wakil Rektor I")
tree_dosen.insert_node("R001", "WR2", "Wakil Rektor II")
tree_dosen.insert_node("R001", "WR3", "Wakil Rektor III")
tree_dosen.insert_node("R001", "D001", "Dekan Fakultas Sains dan Teknologi")

# Anak Dekan
tree_dosen.insert_node("D001", "WD1", "Wakil Dekan I")
tree_dosen.insert_node("D001", "WD2", "Wakil Dekan II")
tree_dosen.insert_node("D001", "WD3", "Wakil Dekan III")
tree_dosen.insert_node("D001", "KPI001", "Ketua Program Studi Teknik Informatika")

# Anak Ketua Program Studi
tree_dosen.insert_node("KPI001", "SP001", "Sekretaris Program Studi")
tree_dosen.insert_node("KPI001", "LAB001", "Kepala Laboratorium Komputer")
tree_dosen.insert_node("KPI001", "KD001", "Koordinator Dosen")

# Anak Kepala Laboratorium
tree_dosen.insert_node("LAB001", "AL001", "Asisten Laboratorium")
tree_dosen.insert_node("LAB001", "TL001", "Teknisi Laboratorium")

# Anak Koordinator Dosen
tree_dosen.insert_node("KD001", "DPA001", "Dosen Pembimbing Akademik")
tree_dosen.insert_node("KD001", "DPM001", "Dosen Pengampu Mata Kuliah")

# Anak Dosen Pembimbing Akademik
tree_dosen.insert_node("DPA001", "MB001", "Mahasiswa Bimbingan")


print("\nTRAVERSAL STRUKTUR ORAGANISASI BARU NO 11")

print("\nPre-Order:")
tree_dosen.preorder(tree_dosen.root)

print("\nIn-Order:")
tree_dosen.inorder(tree_dosen.root)

print("\nPost-Order:")
tree_dosen.postorder(tree_dosen.root)