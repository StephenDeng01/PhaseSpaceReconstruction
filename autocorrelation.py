import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


def auto_correlation(signal, t):
    avg = np.mean(signal)
    numerator = sum((signal[i] - avg) * (signal[i + t] - avg) for i in range(len(signal) - t))
    denominator = sum((x - avg) ** 2 for x in signal)
    return numerator / denominator if denominator != 0 else 0


if __name__ == '__main__':
    # 更具代表性的周期信号
    test_signal = np.sin(2 * np.pi * np.arange(757) / 50)

    t_list = range(70)
    y = [auto_correlation(test_signal, t) for t in t_list]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(t_list, y, label='自相关函数', color='blue', linestyle='-', linewidth=2,
            marker='o', markersize=3, alpha=0.7)

    ax.set_title('延迟参数-自相关函数值', fontsize=16, pad=20)
    ax.set_xlabel('延迟参数', fontsize=14, labelpad=10)
    ax.set_ylabel('自相关函数值', fontsize=14, labelpad=10)

    ax.set_xlim(0, 75)
    ax.set_ylim(-1, 1)
    ax.set_xticks(np.arange(0, 75, 5))
    ax.set_yticks(np.arange(-1, 2, 1))
    ax.legend(fontsize=12, loc='upper right')

    plt.show()
