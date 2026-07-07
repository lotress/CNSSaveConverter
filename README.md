# CNS save file JSON converter / CNS存档JSON转换器

## Introduction / 介绍

[CNS - Custom Nanosuit System](https://www.nexusmods.com/stellarblade/mods/1496) broke my save file. I was about to lose hundreds of outfit saves that took days to craft ...or... I made this tool to fix it all. This tool converts CNS save files to JSON and back, so you can safely inspect and edit your save data with any text editor.

[CNS - Custom Nanosuit System](https://www.nexusmods.com/stellarblade/mods/1496)把我的存档弄坏了。我注定要告别花费好几天时间雕琢出来的几百套服装存档...或者...我做了这个工具来修复这一切。这个工具可以在CNS存档与JSON格式之间双向转换，现在亲爱的玩家朋友可以用任意文本编辑器修改存档文件。

The source code is published on [my Github](https://github.com/lotress/CNSSaveConverter).

源代码发布在[我的Github](https://github.com/lotress/CNSSaveConverter)。

## ⚠️ Disclaimer / 注意

This tool is entirely based on reverse-engineering of the CNS save file format. I did not have access to CNS design documentation, so this implementation may be incomplete. Use it at your own risk. After saving a file you should immediately verify it in-game. Before overwriting any existing save, this tool automatically creates a backup in a `backup` folder next to the save file.

本工具完全来自对CNS存档文件的逆向分析，我没有获得CNS的设计资料，这里的实现可能存在缺失。请自行承担风险，保存存档后应立即进入游戏验证，覆盖已有存档前本工具会自动备份存档，备份位于存档位置的backup文件夹下。

## Installation / 安装方式

I provide both a standalone command-line program and a [Mod Organizer](https://www.modorganizer.org/) plugin version. For the standalone program, download the archive and extract it to a regular directory. For the Mod Organizer plugin, extract it under Mod Organizer's `plugins\` directory.

我提供了独立运行的命令行程序和[Mod Organizer](https://www.modorganizer.org/)插件版本。对于独立程序，下载压缩包后解压到普通目录中，Mod Organizer插件则解压到Mod Organizer的`plugins\`下面。

## Usage / 使用方式


### Standalone Program / 独立程序

Command format / 命令格式:

```bash
CNSSaveConverter [-h] [-i INDENT] [-v] {tojson,fromjson} input output
```

Parameters / 参数说明:

```bash
positional arguments:
  {tojson,fromjson}     Command to execute
  input                 Input file path
  output                Output file path

options:
  -h, --help            show this help message and exit
  -i INDENT, --indent INDENT
                        JSON indent level (tojson only) (default: 2)
  -v, --version         show program's version number and exit
```

### Mod Organizer Plugin / Mod Organizer插件

Click `CNS save file JSON converter` in the toolbar under `Plugins`. The plugin will open dialogs to select the input file and the output file path in sequence.

在`工具栏-插件`里点击`CNS save file JSON converter`。选择输入文件和输出文件的对话框会依次打开。