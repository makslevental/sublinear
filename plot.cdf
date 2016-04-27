(* Content-type: application/vnd.wolfram.cdf.text *)

(*** Wolfram CDF File ***)
(* http://www.wolfram.com/cdf *)

(* CreatedBy='Mathematica 10.1' *)

(*************************************************************************)
(*                                                                       *)
(*  The Mathematica License under which this file was created prohibits  *)
(*  restricting third parties in receipt of this file from republishing  *)
(*  or redistributing it by any means, including but not limited to      *)
(*  rights management or terms of use, without the express consent of    *)
(*  Wolfram Research, Inc. For additional information concerning CDF     *)
(*  licensing and redistribution see:                                    *)
(*                                                                       *)
(*        www.wolfram.com/cdf/adopting-cdf/licensing-options.html        *)
(*                                                                       *)
(*************************************************************************)

(*CacheID: 234*)
(* Internal cache information:
NotebookFileLineBreakTest
NotebookFileLineBreakTest
NotebookDataPosition[      1064,         20]
NotebookDataLength[      5178,        162]
NotebookOptionsPosition[      5496,        149]
NotebookOutlinePosition[      5997,        171]
CellTagsIndexPosition[      5954,        168]
WindowFrame->Normal*)

(* Beginning of Notebook Content *)
Notebook[{
Cell[BoxData[
 RowBox[{
  RowBox[{"f", "[", 
   RowBox[{"n_", ",", "l_", ",", "e_"}], "]"}], ":=", 
  RowBox[{
   SqrtBox[
    FractionBox["n", "l"]], 
   SuperscriptBox["e", 
    RowBox[{"-", "4.5"}]], 
   SuperscriptBox[
    RowBox[{"Log", "[", "n", "]"}], "2"], 
   RowBox[{"Log", "[", 
    FractionBox["1", "e"], "]"}]}]}]], "Input", "PluginEmbeddedContent"],

Cell[BoxData[
 RowBox[{
  RowBox[{"l", "[", "e_", "]"}], ":=", 
  RowBox[{"n", "/.", 
   RowBox[{
    RowBox[{"NSolve", "[", 
     RowBox[{
      RowBox[{
       RowBox[{
        RowBox[{"f", "[", 
         RowBox[{"n", ",", "1", ",", "e"}], "]"}], "/", "n"}], "\[Equal]", 
       "1"}], ",", "n"}], "]"}], "[", 
    RowBox[{"[", "3", "]"}], "]"}]}]}]], "Input", "PluginEmbeddedContent"],

Cell[BoxData[
 RowBox[{
  RowBox[{"ff", "[", "e_", "]"}], ":=", 
  RowBox[{"Quiet", "[", 
   RowBox[{
    RowBox[{"Plot", "[", 
     RowBox[{
      RowBox[{"{", 
       RowBox[{
        RowBox[{
         RowBox[{"f", "[", 
          RowBox[{"n", ",", "1", ",", "e"}], "]"}], "/", "n"}], ",", "0"}], 
       "}"}], ",", 
      RowBox[{"{", 
       RowBox[{"n", ",", "1", ",", 
        RowBox[{"x", "*", "10"}]}], "}"}], ",", "\[IndentingNewLine]", 
      RowBox[{"AspectRatio", "\[Rule]", "Full"}], ",", 
      RowBox[{"PlotLegends", "\[Rule]", 
       RowBox[{"{", 
        RowBox[{"\"\<error\>\"", " ", "e"}], "}"}]}], ",", 
      "\[IndentingNewLine]", 
      RowBox[{"Epilog", "\[Rule]", 
       RowBox[{"{", 
        RowBox[{
         RowBox[{"Line", "[", 
          RowBox[{"{", 
           RowBox[{
            RowBox[{"{", 
             RowBox[{"x", ",", "0"}], "}"}], ",", 
            RowBox[{"{", 
             RowBox[{"x", ",", "1"}], "}"}]}], "}"}], "]"}], ",", 
         "\[IndentingNewLine]", 
         RowBox[{"Text", "[", 
          RowBox[{
           RowBox[{"\"\<break even \>\"", "x"}], ",", 
           RowBox[{"{", 
            RowBox[{
             RowBox[{"x", "*", "4"}], ",", "1"}], "}"}]}], "]"}]}], "}"}]}]}],
      "]"}], "\[IndentingNewLine]", "/.", 
    RowBox[{
     RowBox[{"NSolve", "[", 
      RowBox[{
       RowBox[{
        RowBox[{
         RowBox[{"f", "[", 
          RowBox[{"x", ",", "1", ",", "e"}], "]"}], "/", "x"}], "\[Equal]", 
        "1"}], ",", "x"}], "]"}], "[", 
     RowBox[{"[", "3", "]"}], "]"}]}], "]"}]}]], "Input", \
"PluginEmbeddedContent"],

Cell[CellGroupData[{

Cell[BoxData["\[IndentingNewLine]"], "Input", "PluginEmbeddedContent"],

Cell[BoxData[
 TagBox[
  StyleBox[
   DynamicModuleBox[{$CellContext`e$$ = 0.05, Typeset`show$$ = True, 
    Typeset`bookmarkList$$ = {}, Typeset`bookmarkMode$$ = "Menu", 
    Typeset`animator$$, Typeset`animvar$$ = 1, Typeset`name$$ = 
    "\"untitled\"", Typeset`specs$$ = {{
      Hold[$CellContext`e$$], 0.05, 0.49}}, Typeset`size$$ = {
    472., {213., 219.}}, Typeset`update$$ = 0, Typeset`initDone$$, 
    Typeset`skipInitDone$$ = True, $CellContext`e$227237$$ = 0}, 
    DynamicBox[Manipulate`ManipulateBoxes[
     1, StandardForm, "Variables" :> {$CellContext`e$$ = 0.05}, 
      "ControllerVariables" :> {
        Hold[$CellContext`e$$, $CellContext`e$227237$$, 0]}, 
      "OtherVariables" :> {
       Typeset`show$$, Typeset`bookmarkList$$, Typeset`bookmarkMode$$, 
        Typeset`animator$$, Typeset`animvar$$, Typeset`name$$, 
        Typeset`specs$$, Typeset`size$$, Typeset`update$$, Typeset`initDone$$,
         Typeset`skipInitDone$$}, "Body" :> $CellContext`ff[$CellContext`e$$],
       "Specifications" :> {{$CellContext`e$$, 0.05, 0.49}}, "Options" :> {}, 
      "DefaultOptions" :> {}],
     ImageSizeCache->{519., {257., 264.}},
     SingleEvaluation->True],
    Deinitialization:>None,
    DynamicModuleValues:>{},
    SynchronousInitialization->True,
    UndoTrackedVariables:>{Typeset`show$$, Typeset`bookmarkMode$$},
    UnsavedVariables:>{Typeset`initDone$$},
    UntrackedVariables:>{Typeset`size$$}], "Manipulate",
   Deployed->True,
   StripOnInput->False],
  Manipulate`InterpretManipulate[1]]], "Output", "PluginEmbeddedContent"]
}, Open  ]]
},
WindowSize->{554.38, 761.69},
Visible->True,
AuthoredSize->{554, 762},
ScrollingOptions->{"HorizontalScrollRange"->Fit,
"VerticalScrollRange"->Fit},
ShowCellBracket->False,
Deployed->True,
CellContext->Notebook,
TrackCellChangeTimes->False,
FrontEndVersion->"10.1 for Linux x86 (64-bit) (March 23, 2015)",
StyleDefinitions->"Default.nb"
]
(* End of Notebook Content *)

(* Internal cache information *)
(*CellTagsOutline
CellTagsIndex->{}
*)
(*CellTagsIndex
CellTagsIndex->{}
*)
(*NotebookFileOutline
Notebook[{
Cell[1464, 33, 362, 12, 61, "Input"],
Cell[1829, 47, 387, 12, 17, "Input"],
Cell[2219, 61, 1600, 48, 106, "Input"],
Cell[CellGroupData[{
Cell[3844, 113, 70, 0, 40, "Input"],
Cell[3917, 115, 1563, 31, 523, "Output"]
}, Open  ]]
}
]
*)

(* End of internal cache information *)

(* NotebookSignature cuTwzkX8#aTmgBw23mnj8vom *)
