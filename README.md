# Stellar Blade save file JSON converter / Stellar Blade存档JSON转换器

## Introduction / 介绍

[CNS - Custom Nanosuit System](https://www.nexusmods.com/stellarblade/mods/1496) broke my save file. I was about to lose hundreds of outfit saves that took days to craft ...or... I made this tool to fix it all. This tool converts save files of Stellar Blade & Mods to JSON and back, so you can safely inspect and edit your save data with any text editor.

After upgrading to version 2.0, this tool supports saving and loading conversions for the game itself and many mods. Of course, I haven't seen all mods, so there might be some that it cannot handle. Additionally, the new version is not compatible with JSON files exported by the old version. You'll need to use the new version to convert saves to JSON.

The source code is published on [my Github](https://github.com/lotress/CNSSaveConverter). You can also download the release file from Github if it's quarantined on nexusmods.

[CNS - Custom Nanosuit System](https://www.nexusmods.com/stellarblade/mods/1496)把我的存档弄坏了。我注定要告别花费好几天时间雕琢出来的几百套服装存档...或者...我做了这个工具来修复这一切。这个工具可以在剑星及各种Mod的存档与JSON格式之间双向转换，现在亲爱的玩家朋友可以用任意文本编辑器修改存档文件。

升级到2.0版本后，这个工具支持游戏本身和许多Mod的存档转换，当然我没见过所有Mod，可能存在无法处理的。另外新版本不兼容旧版本输出的JSON文件，你需要用新版本从存档转换为JSON。

源代码发布在[我的Github](https://github.com/lotress/CNSSaveConverter)。如果在nexusmods的文件下载被隔离中，你也可以去Github的Release页面下载。

## About corrupted CNS file and how I fixed it / 我是怎么修复的

At some point, changing outfits with CNS visually appeared to work, but the internal CNS data was not updated. In that state, saving a preset file would only write the old fixed outfit, and loading the save would restore the old appearance. This means the CNS save file (`DekCNS.sav`) had become corrupted, and it could not be fixed from within the game.

I converted both the corrupted save and a good initial save to JSON, then replaced top-level properties in the bad save piece by piece. I eventually found that removing the `AutoLoadCNS` and `CamPosition` properties allowed CNS to save correctly again. Compared with presets, these two properties are just negligible. I still do not understand why this works, but since it does, I implemented the fix in this tool so you can try it if you see the same issue, just run the command line program with `fix` command on your save file. Of course, it may not work in every case, so please share any failure examples.

在某一时刻，用CNS更换服装虽然视觉上正常改变但CNS的内部数据没有更新，此时保存预置档将只能写入固定的旧服装，并且载入存档后外观也会恢复成旧的。这意味着CNS存档文件（DekCNS.sav）已经损坏，在游戏中操作无法修正。
我将损坏存档和一个好的初始存档都转换为JSON，分部替换坏存档的顶级属性，直到发现删除"AutoLoadCNS"和"CamPosition"这两个属性之后CNS能够正常保存了，跟预置档相比这两个选项无足轻重。我完全不能理解这一切的原因，但既然这么做有效，那我就在程序里实现了这个功能，出现同样的现象时你也可以试试，命令行程序以fix命令执行，输入你的存档文件。当然这么做也可能无效，你可以分享失效的案例。

## ⚠️ Disclaimer / 注意

This tool is entirely based on reverse-engineering of Stellar Blade save file format and this implementation may be incomplete. The save files have strict requirements on data types, and consistency must be maintained when editing JSON. Use it at your own risk. After saving a file you should immediately verify it in-game. Before overwriting any existing save, this tool automatically creates a backup in a `backup` folder next to the save file.

本工具完全来自对剑星存档文件的逆向分析，我没有获得存档文件格式的设计资料，这里的实现可能存在缺失。存档文件对于数据类型有严格要求，编辑JSON时需保持一致。请自行承担风险，保存存档后应立即进入游戏验证，覆盖已有存档前本工具会自动备份存档，备份位于存档位置的backup文件夹下。

## Installation / 安装方式

I provide both a standalone command-line program and a [Mod Organizer](https://www.modorganizer.org/) plugin version. For the standalone program, download the archive and extract it to a regular directory. For the Mod Organizer plugin, extract it under Mod Organizer's `plugins\` directory, delete the old `CNSSaveConverter` folder if exists.

我提供了独立运行的命令行程序和[Mod Organizer](https://www.modorganizer.org/)插件版本。对于独立程序，下载压缩包后解压到普通目录中，Mod Organizer插件则解压到Mod Organizer的`plugins\`下面，旧版本的`CNSSaveConverter`目录可以删掉。

## Usage / 使用方式

### Standalone Program / 独立程序

Command format / 命令格式:

```bash
SBSaveConverter [-h] [-i INDENT] [-v] {tojson,fromjson,fix} input output
```

Parameters / 参数说明:

```bash
positional arguments:
  {tojson,fromjson,fix}
                        Command to execute
  input                 Input file path
  output                Output file path (not required for fix) (default: None)

options:
  -h, --help            show this help message and exit
  -i INDENT, --indent INDENT
                        JSON indent level (tojson only) (default: 2)
  -v, --version         show program's version number and exit
```

### Mod Organizer Plugin / Mod Organizer插件

Click `Stellar Blade save file JSON converter` in the toolbar under `Plugins`. The plugin will open dialogs to select the input file and the output file path in sequence.

在`工具栏-插件`里点击`Stellar Blade save file JSON converter`。选择输入文件和输出文件的对话框会依次打开。