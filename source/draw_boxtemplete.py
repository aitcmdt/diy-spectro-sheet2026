import matplotlib.patches as patches
import matplotlib.pyplot as plt

A4_WIDTH_CM = 29.7
A4_HEIGHT_CM = 21.0

# 印刷補正係数
SCALE_FACTOR = 10.0 / 9.5

# 用紙中心を基準にスケーリング
CENTER_X = A4_WIDTH_CM / 2.0
CENTER_Y = A4_HEIGHT_CM / 2.0


def scale_point(x, y):
    new_x = CENTER_X + (x - CENTER_X) * SCALE_FACTOR
    new_y = CENTER_Y + (y - CENTER_Y) * SCALE_FACTOR
    return new_x, new_y


def scale_points(pts):
    return [scale_point(x, y) for x, y in pts]


fig = plt.figure(figsize=(A4_WIDTH_CM / 2.54, A4_HEIGHT_CM / 2.54))
ax = fig.add_axes([0, 0, 1, 1])

# 1. 外形ポリゴン
poly_points = [
    (7.0, 2.25),
    (7.0, 3.0),
    (4.0, 3.0),
    (4.0, 6.867),
    (6.5, 6.867),
    (6.5, 7.0),
    (4.0, 7.0),
    (4.0, 8.0),
    (6.25, 8.0),
    (6.25, 16.0),
    (3.5, 16.0),
    (3.5, 19.0),
    (17.75, 19.0),
    (17.75, 11.0),
    (22.0, 11.0),
    (22.0, 8.0),
    (21.0, 8.0),
    (21.0, 10.0),
    (20.0, 10.0),
    (20.0, 8.0),
    (18.0, 8.0),
    (18.0, 3.0),
    (17.0, 3.0),
    (17.0, 2.25),
]
scaled_poly = scale_points(poly_points)
ax.add_patch(
    patches.Polygon(
        scaled_poly, closed=True, fill=False, edgecolor="black", linewidth=1.5
    )
)

# 2. 切り込み線（実線）
cut_lines = [
    ((7.0, 8.0), (6.25, 8.0)),
    ((7.0, 11.0), (6.25, 11.0)),
    ((7.0, 16.0), (6.25, 16.0)),
    ((17.0, 8.0), (18.0, 8.0)),
    ((17.0, 11.0), (17.75, 11.0)),
    ((17.0, 16.0), (17.75, 16.0)),
]
for p1, p2 in cut_lines:
    sp1 = scale_point(*p1)
    sp2 = scale_point(*p2)
    ax.plot([sp1[0], sp2[0]], [sp1[1], sp2[1]], color="black", linewidth=1.5)

# 3. 折り線（破線）
fold_lines = [
    ((7.0, 3.0), (7.0, 19.0)),
    ((17.0, 3.0), (17.0, 19.0)),
    ((7.0, 3.0), (17.0, 3.0)),
    ((7.0, 8.0), (17.0, 8.0)),
    ((7.0, 11.0), (17.0, 11.0)),
    ((7.0, 16.0), (17.0, 16.0)),
]
for p1, p2 in fold_lines:
    sp1 = scale_point(*p1)
    sp2 = scale_point(*p2)
    ax.plot(
        [sp1[0], sp2[0]],
        [sp1[1], sp2[1]],
        color="#555555",
        linewidth=1.2,
        linestyle=(0, (4, 3)),
    )

# 4. 寸法線（10cm幅: 5mm下に移動 y=1.0 -> y=1.5）
# 矢印両端の補助線（縦線）
aux1_p1, aux1_p2 = scale_point(7.0, 1.25), scale_point(7.0, 1.75)
ax.plot(
    [aux1_p1[0], aux1_p2[0]], [aux1_p1[1], aux1_p2[1]], color="black", linewidth=1.0
)

aux2_p1, aux2_p2 = scale_point(17.0, 1.25), scale_point(17.0, 1.75)
ax.plot(
    [aux2_p1[0], aux2_p2[0]], [aux2_p1[1], aux2_p2[1]], color="black", linewidth=1.0
)

# 両矢印線
sp1 = scale_point(7.0, 1.5)
sp2 = scale_point(17.0, 1.5)
ax.annotate(
    "",
    xy=sp1,
    xytext=sp2,
    arrowprops=dict(
        arrowstyle="<->", color="black", linewidth=1.2, shrinkA=0, shrinkB=0
    ),
)

# 寸法テキスト（y=1.1に配置）
t_pos = scale_point(12.0, 1.1)
ax.text(
    t_pos[0],
    t_pos[1],
    "10cm",
    ha="center",
    va="bottom",
    fontsize=12 * SCALE_FACTOR,
)

# 5. 寸法線（8cm高さ）
# 矢印両端の補助線（横線）
aux3_p1, aux3_p2 = scale_point(24.75, 3.0), scale_point(25.25, 3.0)
ax.plot(
    [aux3_p1[0], aux3_p2[0]], [aux3_p1[1], aux3_p2[1]], color="black", linewidth=1.0
)

aux4_p1, aux4_p2 = scale_point(24.75, 11.0), scale_point(25.25, 11.0)
ax.plot(
    [aux4_p1[0], aux4_p2[0]], [aux4_p1[1], aux4_p2[1]], color="black", linewidth=1.0
)

# 両矢印線
sp1 = scale_point(25.0, 3.0)
sp2 = scale_point(25.0, 11.0)
ax.annotate(
    "",
    xy=sp1,
    xytext=sp2,
    arrowprops=dict(
        arrowstyle="<->", color="black", linewidth=1.2, shrinkA=0, shrinkB=0
    ),
)

# 寸法テキスト
t_pos = scale_point(25.5, 7.0)
ax.text(
    t_pos[0],
    t_pos[1],
    "8cm",
    ha="left",
    va="center",
    rotation=-90,
    fontsize=12 * SCALE_FACTOR,
)

# 6. 凡例（きる・おる）
sFold='おる'
sCut='きる'
# sFold='Fold'
# sCut='Cut'

l1_p1, l1_p2 = scale_point(19.25, 15.25), scale_point(20.75, 15.25)
ax.plot(
    [l1_p1[0], l1_p2[0]], [l1_p1[1], l1_p2[1]], color="black", linewidth=1.5
)
t_pos = scale_point(21.2, 15.25)
ax.text(
    t_pos[0],
    t_pos[1],
    sCut,
    va="center",
    fontsize=11 * SCALE_FACTOR,
    fontfamily="TakaoPGothic",
)

l2_p1, l2_p2 = scale_point(19.25, 16.25), scale_point(20.75, 16.25)
ax.plot(
    [l2_p1[0], l2_p2[0]],
    [l2_p1[1], l2_p2[1]],
    color="#555555",
    linewidth=1.2,
    linestyle=(0, (4, 3)),
)
t_pos = scale_point(21.2, 16.25)
ax.text(
    t_pos[0],
    t_pos[1],
    sFold,
    va="center",
    fontsize=11 * SCALE_FACTOR,
    fontfamily="TakaoPGothic",
)

# 用紙境界設定
ax.set_xlim(0, A4_WIDTH_CM)
ax.set_ylim(A4_HEIGHT_CM, 0)
ax.set_aspect("equal")
ax.axis("off")

plt.savefig("spectroscope_prescaled_fixed.pdf", format="pdf")
plt.close()