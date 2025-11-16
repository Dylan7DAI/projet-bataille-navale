# 🚢 Bataille Navale — Projet Python  FR/CN


Un mini-jeu de bataille navale en mode texte utilisant la programmation orientée objet en Python.  
本项目是一个基于 Python 面向对象编程(OOP)的终端海战小游戏。
##  On commence / 快速开始

Télécharger le projet depuis Github.先下载

puis
```bash
cd projet-bataille-navale
```

Créez et activez l'environnement virtuel dans le répertoire du projet :
在项目目录中创建并激活虚拟环境：

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\Activate.ps1      # Windows
```

Installer les dépendances 安装依赖
```bash
pip install -r requirement.txt
```

Exécutez la commande ci‑dessous pour lancer le jeu en mode terminal, puis suivez les invites pour entrer des coordonnées.  
运行下面的命令以在终端中启动游戏，然后按提示输入坐标。
```bash
python Jeu_final.py
```

---


##  Aperçu du jeu / 游戏简介

Le jeu se déroule sur une grille de **8 lignes × 10 colonnes**, contenant **4 bateaux** placés aléatoirement et sans chevauchement : (Le navire de guerre était initialement invisible.) 

游戏基于一个 **8×10 的海图**，其中包含 **4 艘随机生成且不会重叠的战舰**：

| Type de bateau | Longueur | Icône | 说明 |
|----------------|------|--------|------|
| Porte-avion    | 4    | 🚢 | 航母 |
| Croiseur       | 3    | ⛴ | 巡洋舰 |
| Torpilleur     | 2    | 🚣 | 鱼雷快艇 |
| Sous-marin     | 2    | 🐟 | 潜艇 |

###  Mécanique du jeu / 游戏机制

- Entrez des coordonnées `(ligne, colonne)` pour tirer
- Tir manqué → `x`  
- Touché → `💣`  
- Bateau coulé = Touchez toutes les cases du navire → affiche les navires coulés（icône originale🚢⛴🚣🐟）  
- Le jeu se termine une fois les 4 navires de guerre coulés, affichant le nombre total de tirs effectués.  

---


## Prérequis système 系统要求

- **Python 3.7 ou supérieur**
- **Encodage** recommandé UTF-8 (pour afficher correctement les emojis)
- **Système d'exploitation** Windows/Linux/Mac (tout système supportant Python)

## 🎮 Exemple de partie / 游戏示例

Ci-dessous un exemple réel d'une partie jouée dans le terminal :  
下面是一个实际的终端游戏示例：

```
Bienvenue dans la bataille navale !
Grille 8 x 10, 4 bateaux à couler.

~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~

Ligne (1-8)   : 1 （Le numéro que vous avez saisi）
Colonne (1-10): 1 （Le numéro que vous avez saisi）
À l'eau...  （Résultats de tir）

x~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
~~~~~~~~~~
（Nous continuerons d'essayer de tir sur les différentes positions.）
......

Coulé :PorteAvion
x~~x🚢x~x~~
x~~~🚢~⛴⛴⛴~
x~~~🚢~~🚣🚣x
🐟~x~🚢~~x~~
🐟~x~~~~x~~
x~x~~x~x~~
x~x~xx~x~~
x~x~~x~x~~
Bravo ! Vous avez coulé tous les bateaux en 35 coups.

```

##  Auteur / 作者
Huichen DAI


# Finalement, bon jeu!