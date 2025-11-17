import VF2Ismorphism

def main():
    graph1 = [0,0,1,0],[0,0,0,0],[1,0,0,0],[0,0,0,0]
    graph2 = [0,1,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]
    isomorphic = VF2Ismorphism.VF2Isomorphism(graph1, graph2)
    print(f"{isomorphic}")


if __name__ == "__main__":
    main()